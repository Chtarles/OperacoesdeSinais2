from front_operacao_sinais_ import Ui_MainWindow_Operacao_Sinais_
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from OndaResultante import *
from OndaCossenoidal import *
from Verificar import *


class Window_Operacao_Sinais(QMainWindow, Ui_MainWindow_Operacao_Sinais_):
    def __init__(self) -> None:
        super(Window_Operacao_Sinais, self).__init__()
        '''CONECTANDO AO ARQUICO .UI'''
        loadUi("front_operacao_sinais_.ui", self)

        '''TÍTULO DA TELA e ICONE'''
        self.setWindowTitle('Operação de Sinais')
        self.setWindowIcon(QtGui.QIcon('icone_operacao_sinais.png'))

        '''AÇÃO DO BOTÃO PLOT'''
        self.pushButton_Plot_x1.clicked.connect(self.plot_x1)
        self.pushButton_Plot_x2.clicked.connect(self.plot_x2)
        self.pushButton_Plot_result.clicked.connect(self.plot_result)

    def plot_x1(self):
        '''COLETANDO DADOS DA CAIXA DE TEXTO'''
        amp_1 = float(self.spinBox_Amplitude_1.text())
        freq_in_1 = float(self.spinBox_Freq_in_1.text())
        freq_out_1 = int(self.spinBox_Freq_out_1.text())
        tempo_1 = int(self.spinBox_Tempo_1.text())

        if filtro_antialiasing(freq_in_1, freq_out_1):
            '''HERANÇA CLASSE ONDA COSSENOIDAL'''
            y_1, ts_1 = gerar_cos(amp_1, freq_in_1, freq_out_1, tempo_1)

            '''PLOTANDO GRÁFICO NO QWIDGET'''
            if self.radioButton_continuo.isChecked():
                self.MplWidget_1.canvas.axes.clear()
                self.MplWidget_1.canvas.axes.plot(ts_1, y_1)
                self.MplWidget_1.canvas.axes.set(xlabel='Tempo (s)',
                                                 ylabel='Amplitude (V)')
                self.MplWidget_1.canvas.axes.grid()
                self.MplWidget_1.canvas.draw()

            elif self.radioButton_discreto.isChecked():
                self.MplWidget_1.canvas.axes.clear()
                self.MplWidget_1.canvas.axes.stem(ts_1, y_1)
                self.MplWidget_1.canvas.axes.set(xlabel='Tempo (s)',
                                                 ylabel='Amplitude (V)')
                self.MplWidget_1.canvas.axes.grid()
                self.MplWidget_1.canvas.draw()
            elif self.radioButton_quantizado.isChecked():
                self.MplWidget_1.canvas.axes.clear()
                self.MplWidget_1.canvas.axes.step(ts_1, y_1)
                self.MplWidget_1.canvas.axes.set(xlabel='Tempo (s)',
                                                 ylabel='Amplitude (V)')
                self.MplWidget_1.canvas.axes.grid()
                self.MplWidget_1.canvas.draw()
            else:
                mensagem_aviso = QMessageBox(self)
                mensagem_aviso.setWindowTitle('Erro na Plotagem')
                mensagem_aviso.setText('Selecione o tipo de plotagem.\nEntre:\nContínuo\nDiscreto\nQuantizado')
                mensagem_aviso.setIcon(QMessageBox.Warning)
                mensagem_aviso.exec_()
        else:
            mensagem_filtro_antialiasing = QMessageBox(self)
            mensagem_filtro_antialiasing.setWindowTitle('Filtro Anti-Aliasing | Sinal X1')
            mensagem_filtro_antialiasing.setText('Frequência de saída não aceitável.'
                                                 '\nFrequência de saída deve ser maior ou igual a 2X a Frequência de entrada!')
            mensagem_filtro_antialiasing.setIcon(QMessageBox.Warning)
            mensagem_filtro_antialiasing.exec_()

    def plot_x2(self):
        '''COLETANDO DADOS DA CAIXA DE TEXTO'''
        amp_2 = float(self.spinBox_Amplitude_2.text())
        freq_in_2 = float(self.spinBox_Freq_in_2.text())
        freq_out_2 = int(self.spinBox_Freq_out_2.text())
        tempo_2 = int(self.spinBox_Tempo_2.text())

        if filtro_antialiasing(freq_in_2, freq_out_2):
            '''HERANÇA CLASSE ONDA COSSENOIDAL'''
            y_2, ts_2 = gerar_cos(amp_2, freq_in_2, freq_out_2, tempo_2)

            '''PLOTANDO GRÁFICO NO QWIDGET'''
            if self.radioButton_continuo.isChecked():
                self.MplWidget_2.canvas.axes.clear()
                self.MplWidget_2.canvas.axes.plot(ts_2, y_2)
                self.MplWidget_2.canvas.axes.set(xlabel='Tempo (s)',
                                                 ylabel='Amplitude (V)')
                self.MplWidget_2.canvas.axes.grid()
                self.MplWidget_2.canvas.draw()

            elif self.radioButton_discreto.isChecked():
                self.MplWidget_2.canvas.axes.clear()
                self.MplWidget_2.canvas.axes.stem(ts_2, y_2)
                self.MplWidget_2.canvas.axes.set(xlabel='Tempo (s)',
                                                 ylabel='Amplitude (V)')
                self.MplWidget_2.canvas.axes.grid()
                self.MplWidget_2.canvas.draw()

            elif self.radioButton_quantizado.isChecked():
                self.MplWidget_2.canvas.axes.clear()
                self.MplWidget_2.canvas.axes.step(ts_2, y_2)
                self.MplWidget_2.canvas.axes.set(xlabel='Tempo (s)',
                                                 ylabel='Amplitude (V)')
                self.MplWidget_2.canvas.axes.grid()
                self.MplWidget_2.canvas.draw()
            else:
                mensagem_aviso = QMessageBox(self)
                mensagem_aviso.setWindowTitle('Erro na Plotagem')
                mensagem_aviso.setText('Selecione o tipo de plotagem.\nEntre:\nContínuo\nDiscreto\nQuantizado')
                mensagem_aviso.setIcon(QMessageBox.Warning)
                mensagem_aviso.exec_()
        else:
            mensagem_filtro_antialiasing = QMessageBox(self)
            mensagem_filtro_antialiasing.setWindowTitle('Filtro Anti-Aliasing | Sinal X2')
            mensagem_filtro_antialiasing.setText('Frequência de saída não aceitável.'
                                                 '\nFrequência de saída deve ser maior ou igual a 2X a Frequência de entrada!')
            mensagem_filtro_antialiasing.setIcon(QMessageBox.Warning)
            mensagem_filtro_antialiasing.exec_()

    def plot_result(self):
        '''COLETANDO DADOS DA CAIXA DE TEXTO'''
        amp_1 = float(self.spinBox_Amplitude_1.text())
        freq_in_1 = float(self.spinBox_Freq_in_1.text())
        freq_out_1 = int(self.spinBox_Freq_out_1.text())
        tempo_1 = int(self.spinBox_Tempo_1.text())
        y_1, ts_1 = gerar_cos(amp_1, freq_in_1, freq_out_1, tempo_1)

        amp_2 = float(self.spinBox_Amplitude_2.text())
        freq_in_2 = float(self.spinBox_Freq_in_2.text())
        freq_out_2 = int(self.spinBox_Freq_out_2.text())
        tempo_2 = int(self.spinBox_Tempo_2.text())
        y_2, ts_2 = gerar_cos(amp_2, freq_in_2, freq_out_2, tempo_2)

        if validar_plot_resultante(y_1, y_2):
            '''VALIDAÇÃO DE AMPLIFICAÇÃO E DESLOCAMENTO'''
            if self.checkBox_Amplificacao.isChecked():
                amplific = int(self.spinBox_Amplificacao.text())
            else:
                amplific = 1

            if self.checkBox_Deslocamento.isChecked():
                desloc = int(self.spinBox_Deslocamento.text())
            else:
                desloc = 0

            if dif_freq_n(freq_out_1, freq_out_2, tempo_1, tempo_2):
                freq_out = int((freq_out_1 + freq_out_2)/2)
                tempo = int((tempo_1 + tempo_2)/2)
                '''CHAMADA DA FUNÇÃO DE PLOTAGEM DISCRETA'''
                yr, tsr = plot_resultante(y_1, y_2, freq_out, tempo, amplific, desloc)

                '''PLOTANDO GRÁFICO NO QWIDGET'''
                if self.radioButton_continuo.isChecked():
                    self.MplWidget_Result.canvas.axes.clear()
                    self.MplWidget_Result.canvas.axes.plot(tsr, yr)
                    self.MplWidget_Result.canvas.axes.set(xlabel='Tempo (s)',
                                                          ylabel='Amplitude (V)')
                    self.MplWidget_Result.canvas.axes.grid()
                    self.MplWidget_Result.canvas.draw()

                elif self.radioButton_discreto.isChecked():
                    self.MplWidget_Result.canvas.axes.clear()
                    self.MplWidget_Result.canvas.axes.stem(tsr, yr)
                    self.MplWidget_Result.canvas.axes.set(xlabel='Tempo (s)',
                                                          ylabel='Amplitude (V)')
                    self.MplWidget_Result.canvas.axes.grid()
                    self.MplWidget_Result.canvas.draw()

                elif self.radioButton_quantizado.isChecked():
                    self.MplWidget_Result.canvas.axes.clear()
                    self.MplWidget_Result.canvas.axes.step(tsr, yr)
                    self.MplWidget_Result.canvas.axes.set(xlabel='Tempo (s)',
                                                          ylabel='Amplitude (V)')
                    self.MplWidget_Result.canvas.axes.grid()
                    self.MplWidget_Result.canvas.draw()
                else:
                    mensagem_aviso = QMessageBox(self)
                    mensagem_aviso.setWindowTitle('Erro na Plotagem')
                    mensagem_aviso.setText('Selecione o tipo de plotagem.\nEntre:\nContínuo\nDiscreto\nQuantizado')
                    mensagem_aviso.setIcon(QMessageBox.Warning)
                    mensagem_aviso.exec_()
            else:
                mensagem_tempo_saida = QMessageBox(self)
                mensagem_tempo_saida.setWindowTitle('Erro na amostragem')
                mensagem_tempo_saida.setText('O Tempo de Saída da Amostragem dos Sinais são diferentes.'
                                             '\nÉ necessário que as Frequências de Saída sejam iguais.')
                mensagem_tempo_saida.setIcon(QMessageBox.Critical)
                mensagem_tempo_saida.exec_()

        else:
            mensagem_erro_plot = QMessageBox(self)
            mensagem_erro_plot.setWindowTitle('Erro na Plotagem')
            mensagem_erro_plot.setText('Há dados não inseridos!')
            mensagem_erro_plot.setIcon(QMessageBox.Warning)
            mensagem_erro_plot.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_Operacao_Sinais()
    window.show()
    app.exec_()
