from nicegui import ui
import datetime

@ui.page('/cliente_cadastro')
def new_customer_page():
    ui.markdown('# Cadastro Cliente')

    name = ui.input(label='Nome Completo',
                    placeholder='entre com o nome...',
                    on_change=lambda e: e.value)
    
    with ui.input('Aniversário') as date:
        with date.add_slot('append'):
            ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
        with ui.menu() as menu:
            ui.date().bind_value(date)

    document_id = (ui.input(label="CPF",
                            placeholder="entre com o cpf",
                            validation={'Entre com 11 valores para cpf': lambda value: len(value) == 14})
                        .props('mask="###.###.###-##"'))
        
    email = ui.input(label='Email',
                     placeholder='entre com o email...',
                     on_change=lambda e: e.value)


    phone1 = (ui.input(label='Telefone Cel. (WhatsApp)',
                       placeholder='entre com o número de telefone...',
                       validation={'Entre com 14 valores para telefone': lambda value: len(value) == 18},
                       on_change=lambda e: e.value)
                .props('mask="+55(##)# ####-####"'))
     
    phone2 = (ui.input(label='Telefone Comercial',
                       placeholder='entre com o número de telefone...',
                       validation={'Entre com 14 valores para telefone': lambda value: len(value) == 18},
                       on_change=lambda e: e.value)
                .props('mask="+55(##)# ####-####"'))
    
    instagram = ui.input(label='Instagram',
                         placeholder='entre com o @ do instagram...',
                         on_change=lambda e: str(e.value))

    def get_values():
        print(name.value, date.value, document_id.value, phone1.value, phone2.value, instagram.value)

        if name.value and document_id.value:
            ui.notify("Cadastro realizado com sucesso!!")
        else:
            ui.notify("Entre com os dados necessários.", color='red')

    ui.button("Cadastrar!", on_click=get_values)
    ui.button("Início", on_click=lambda: ui.navigate.to('/'))

@ui.page('/cliente')
def customer_page():
    ui.markdown('# Cliente')

ui.markdown('# Boas vindas ao NiceGUI!')

ui.markdown('---')
ui.markdown('## Clientes')
with ui.row():
    ui.button('Cadastrar', on_click=lambda: ui.navigate.to('/cliente_cadastro'))
    ui.button('Buscar', on_click=lambda: ui.navigate.to('/cliente'))

ui.markdown('---')
ui.markdown('## Produtos')
with ui.row():
    ui.button('Cadastrar', on_click=lambda: ui.notify('Cadastrar produto'))
    ui.button('Buscar', on_click=lambda: ui.notify('Buscar produto'))

ui.run()