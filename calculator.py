#codesoft task1 on python programing
"Designing a simple calculator with basic airthmetic operations"
import tkinter as tnr
import math

bgcolor = tnr.Tk()
bgcolor.title('Calculator')
bgcolor.configure(bg='#000000')
bgcolor.resizable(width=False, height=False)


enterfield = tnr.Entry(bgcolor, bg='#008080', fg='#000080', font=('Arial', 25),
                     borderwidth=10, justify="right")
enterfield.grid(row=0, columnspan=10, padx=10, pady=10,
               sticky='n'+'s'+'e'+'w')
enterfield.insert(0, '0')

FONT = ('Arial', 10, 'bold')


class Calculator():
    def __init__(self):
        self.currentvalue = ''
        self.inputvalue = True
        self.result = False

    def Entry(self, value):
        enterfield.delete(0, 'end')
        enterfield.insert(0, value)

    def Enternumber(self, num):
        self.result = False
        fnum = enterfield.get()
        snum = str(num)
        if self.inputvalue:
            self.currentvalue = snum
            self.inputvalue = False
        else:
            self.currentvalue = fnum+snum
        self.Entry(self.currentvalue)

    def StandardOperations(self, val):
        temp_str = enterfield.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str+val)
            self.inputvalue = False
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def ClearEntry(self):
        self.result = False
        self.currentvalue = "0"
        self.Entry(0)
        self.inputvalue = True

    def SquareRoot(self):
        try:
            self.currentvalue = math.sqrt(float(enterfield.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def MPi(self):
        self.result = False
        self.currentvalue = math.pi
        self.Entry(self.current)

    def Ee(self):
        self.result = False
        self.currentvalue = math.e
        self.Entry(self.currentvalue)

    def Degree(self):
        try:
            self.result = False
            self.currentvalue = math.degrees(float(enterfield.get()))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Radiant(self):
        try:
            self.result = False
            self.currentvalue= math.radians(float(enterfield.get()))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Exponen(self):
        try:
            self.result = False
            self.currentvalue = math.exp(float(enterfield.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Factorial(self):
        try:
            self.result = False
            self.currentvalue = math.factorial(float(enterfield.get()))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Sin(self):
        try:
            self.result = False
            self.currentvalue = math.sin(math.radians(float(enterfield.get())))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Cos(self):
        try:
            self.result = False
            self.currentvalue= math.cos(math.radians(float(enterfield.get())))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Tan(self):
        try:
            self.result = False
            self.currentvalue= math.tan(math.radians(float(enterfield.get())))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Sinh(self):
        try:
            self.result = False
            self.currentvalue = math.sinh(math.radians(float(enterfield.get())))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Cosh(self):
        try:
            self.result = False
            self.currentvalue = math.cosh(math.radians(float(enterfield.get())))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Tanh(self):
        try:
            self.result = False
            self.currentvalue = math.tanh(math.radians(float(enterfield.get())))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Ln(self):
        try:
            self.result = False
            self.currentvalue = math.log(float(enterfield.get()))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Log_10(self):
        try:
            self.result = False
            self.currentvalue = math.log10(float(enterfield.get()))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Log_2(self):
        try:
            self.result = False
            self.currentvalue = math.log2(float(enterfield.get()))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Pow_2(self):
        try:
            self.result = False
            self.currentvalue = int(enterfield.get())**2
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Pow_3(self):
        try:
            self.result = False
            self.currentvalue = int(enterfield.get())**3
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Pow_10_n(self):
        try:
            self.result = False
            self.currentvalue = 10**int(enterfield.get())
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def One_div_x(self):
        try:
            self.result = False
            self.currentvalue = 1/(int(enterfield.get()))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Abs(self):
        try:
            self.result = False
            self.currentvalue = abs(float(enterfield.get()))
            self.Entry(self.currentvalue)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')


number= "789456123"
l = 0
but = []
for m in range(2, 5):
    for n in range(3):
        but.append(tnr.Button(bgcolor, text=number[l], font=FONT,
                                fg="red", width=6, height=2,
                                highlightbackground='#ADD8E6', highlightthickness=2))
        but[l].grid(row=m, column=n, sticky='n' +
                       's'+'e' + 'w', padx=10, pady=10)
        but[l]["command"] = lambda x=number[l]: sc_app.Enternumber(x)
        l += 1


buttonclear = tnr.Button(bgcolor, text='Clear', command=lambda: sc_app.ClearEntry(),
                   font=FONT, height=2, fg="#000000",
                   highlightbackground='#008080', highlightthickness=2)
buttonclear.grid(row=1, column=0, columnspan=2,
            sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonsquare = tnr.Button(bgcolor, text='\u221A', command=lambda: sc_app.SquareRoot(),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttonsquare.grid(row=1, column=2, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonzero = tnr.Button(bgcolor, text='0', command=lambda: sc_app.Enternumber('0'),
                  font=FONT, width=6, height=2, fg="#000000",
                  highlightbackground='#ADD8E6', highlightthickness=2)
buttonzero.grid(row=5, column=0, columnspan=2,
           sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonpoint = tnr.Button(bgcolor, text='.', command=lambda: sc_app.StandardOperations('.'),
                      font=FONT, width=6, height=2, fg="#000000",
                      highlightbackground='#ADD8E6', highlightthickness=2)
buttonpoint.grid(row=5, column=2, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonequalto = tnr.Button(bgcolor, text='=', command=lambda: sc_app.StandardOperations('='),
                      font=FONT, width=6, height=2, fg="#000000",
                      highlightbackground='#ADD8E6', highlightthickness=2)
buttonequalto.grid(row=5, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonsum = tnr.Button(bgcolor, text='+', command=lambda: sc_app.StandardOperations('+'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttonsum.grid(row=1, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonsub = tnr.Button(bgcolor, text='-', command=lambda: sc_app.StandardOperations('-'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttonsub.grid(row=2, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonmul = tnr.Button(bgcolor, text='*', command=lambda: sc_app.StandardOperations('*'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttonmul.grid(row=3, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttondiv = tnr.Button(bgcolor, text='/', command=lambda: sc_app.StandardOperations('/'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttondiv.grid(row=4, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonpi = tnr.Button(bgcolor, text='\u03C0', command=lambda: sc_app.MPi(),
                   font=FONT, width=5, height=2, fg="#000000",
                   highlightbackground='#ADD8E6', highlightthickness=2)
buttonpi.grid(row=1, column=4, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttone = tnr.Button(bgcolor, text='e', command=lambda: sc_app.Ee(),
                  font=FONT, width=5, height=2, fg="#000000",
                  highlightbackground='#ADD8E6', highlightthickness=2)
buttone.grid(row=1, column=5, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttondeg = tnr.Button(bgcolor, text='Deg', command=lambda: sc_app.Degree(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttondeg.grid(row=1, column=6, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonexp = tnr.Button(bgcolor, text='Exp', command=lambda: sc_app.Exponen(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttonexp.grid(row=2, column=4, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonfact = tnr.Button(bgcolor, text='!', command=lambda: sc_app.Factorial(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
buttonfact.grid(row=2, column=5, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonrad = tnr.Button(bgcolor, text='Rad', command=lambda: sc_app.Radiant(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttonrad.grid(row=2, column=6, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonsin = tnr.Button(bgcolor, text='sin', command=lambda: sc_app.Sin(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttonsin.grid(row=3, column=4, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttoncos = tnr.Button(bgcolor, text='cos', command=lambda: sc_app.Cos(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttoncos.grid(row=3, column=5, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttontan = tnr.Button(bgcolor, text='tan', command=lambda: sc_app.Tan(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttontan.grid(row=3, column=6, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonsinh = tnr.Button(bgcolor, text='sinh', command=lambda: sc_app.Sinh(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
buttonsinh.grid(row=4, column=4, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttoncosh = tnr.Button(bgcolor, text='cosh', command=lambda: sc_app.Cosh(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
buttoncosh.grid(row=4, column=5, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttontanh = tnr.Button(bgcolor, text='tanh', command=lambda: sc_app.Tanh(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
buttontanh.grid(row=4, column=6, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonln = tnr.Button(bgcolor, text='ln', command=lambda: sc_app.Ln(),
                   font=FONT, width=5, height=2, fg="#000000",
                   highlightbackground='#ADD8E6', highlightthickness=2)
buttonln.grid(row=5, column=4, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonlog2 = tnr.Button(bgcolor, text='log2', command=lambda: sc_app.Log_2(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
buttonlog2.grid(row=5, column=5, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonlog10 = tnr.Button(bgcolor, text='log10', command=lambda: sc_app.Log_10(),
                      font=FONT, width=5, height=2, fg="#000000",
                      highlightbackground='#ADD8E6', highlightthickness=2)
buttonlog10.grid(row=5, column=6, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonxpow2 = tnr.Button(bgcolor, text='x\u00B2', command=lambda: sc_app.Pow_2(),
                       font=FONT, width=5, height=2, fg="#000000",
                       highlightbackground='#ADD8E6', highlightthickness=2)
buttonxpow2.grid(row=1, column=7, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonxpow3 = tnr.Button(bgcolor, text='x\u00B3', command=lambda: sc_app.Pow_3(),
                       font=FONT, width=5, height=2, fg="#000000",
                       highlightbackground='#ADD8E6', highlightthickness=2)
buttonxpow3.grid(row=2, column=7, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

button10pow_n = tnr.Button(bgcolor, text='10\u207F', command=lambda: sc_app.Pow_10_n(),
                         font=FONT, width=5, height=2, fg="#000000",
                         highlightbackground='#ADD8E6', highlightthickness=2)
button10pow_n.grid(row=3, column=7, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttononedivx = tnr.Button(bgcolor, text='1/x', command=lambda: sc_app.One_div_x(),
                          font=FONT, width=5, height=2, fg="#000000",
                          highlightbackground='#ADD8E6', highlightthickness=2)
buttononedivx.grid(row=4, column=7, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

buttonabs = tnr.Button(bgcolor, text='Abs', command=lambda: sc_app.Abs(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
buttonabs.grid(row=5, column=7, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

if __name__ == '__main__':

    sc_app = Calculator()

    bgcolor.mainloop()
