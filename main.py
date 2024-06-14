import PySimpleGUI as ys #importando biblioteca como "ys"
import time

def windowRegister(): # criando uma function que gera tela de registro
    ys.theme('Black')
    layout = [[ys.Text('Cadastro', size=(60, 2), font=60, justification='c')],
              [ys.Text('E-mail'), ys.Input(key='email')],
              [ys.Text('Reinsira e-mails'), ys.Input(key='Remail')],
              [ys.Text('Criar nome de usuario'), ys.Input(key='user')],
              [ys.Text('Criar Senha'), ys.Input(key='pass', password_char='*')],
              [ys.Checkbox('salvar senha')],
              [ys.Button('Register'), ys.Button('Sair')]]

    # retorno a tela com o layout e com parâmetro true para poder chamar e navegar entre as telas
    return ys.Window('Register Page', layout, finalize=True)


def windowLogin(): #criando uma function que gera tela de login
    layout = [[ys.Text('Login', size=(60, 2), font=60, justification='c')],
              [ys.Text('Usuario'), ys.Input(key='user_login')],
              [ys.Text('Senha'), ys.Input(key='pass_login', password_char='*')],
              [ys.Checkbox('salvar senha')],
              [ys.Button('Login'), ys.Button('Sair')]]

    # retorno a tela com o layout e com parâmetro true para poder chamar e navegar entre as telas
    return ys.Window('Login Page', layout, finalize=True)

def loadingBar(): # definindo uma funçao tela de carregamento
    layout = [
        [ys.Text('Progresso:')],
        [ys.ProgressBar(100, orientation='h', size=(20, 20), key='PROGRESS')],
        ]
    return ys.Window('Loading Bar', layout, finalize=True) # retorno a tela com o layout e com parâmetro true para poder chamar e navegar entre as telas

#Inicio a janela1 como a function de tela de registro e a segunda deixo como vazia pois não quero mostrá-la agora
janela1, janela2,loadingbar = windowRegister(), None, None #atribuindo a janela 1 a tela de registro e a segunda janela como vazia
while True: #enquanto for true
    janelaAtiva, event, values = ys.read_all_windows() #atribuindo a janela ativa, os eventos das telas e os valores as variáveis

    if janelaAtiva == janela1 and event == ys.WINDOW_CLOSED: #se a janelaAtiva for igual a janela 1 e o evento for fechar vai dar o break
        break
    elif janelaAtiva == janela2 and event == ys.WINDOW_CLOSED: #se a janela ativa for igual a janela2 e o evento for fechar ela vai dar o break
        break
    if event == 'Sair':
        break
    if janelaAtiva == janela1 and event == 'Register': #se a janela ativa for igual a janela 1 e o evento for clicar em registrar vai registrar

        email_current = values['email'] #guardando os dados do email
        user_current = values['user'] #guardando os dados do user
        password_current = values['pass'] #guardando os dados da senha
        password_current = values['pass'] #guardando os dados da senha
        print(user_current, password_current)
        janela1.hide()  # escondendo a janela 1


        loadingbar = loadingBar() # alocando a var da linha 36 a funçao de mostrar a tela da loadingbar
        loadingbar.bring_to_front() # trazendo a loading bar pra frent
        for i in range(100): # ir de 0 (i) ate 100 (range)
            loadingbar['PROGRESS'].update(i + 1) # incrementaçao da chave da loading bar da linha 31
            ys.popup_animated(None, message='Aguarde...', background_color='white') #criando um popup para a loading bar
            time.sleep(0.1) # tempo de carregamento

        loadingbar.close() # fechar a loading bar quando carregar

        janela2 = windowLogin() #atribuindo um valor a janela2 q estava none

    if(event == 'Login'): #se o evento for clicar em login
        if values['user_login'] != user_current or values['pass_login'] != password_current: #se os valores de user login for diferente do user salvo e a senha
            ys.popup("User or Password incorrect") #vai abrir um popup com senha incorreta
            print("Username or Password incorret!")
        elif values['user_login'] == user_current and values['pass_login'] == password_current:
            print("Login Successful")
            ys.popup("Login Successful")