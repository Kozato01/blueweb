import streamlit as st
from styler import customize_style  # Supondo que você tenha uma função para personalizar o estilo
import random

def main():
    # Configuração da página
    st.set_page_config(page_title="Cadastro de Operadora - BLUENETS", page_icon=":globe_with_meridians:", layout="wide")
    col1, col2, col3 = st.columns([1, 2, 1])
    promos_sets = [
        [
            "- **Internet 500MB:** Navegue com ultra velocidade por apenas R$99,90/mês!",
            "- **Pacotes Família:** Descontos exclusivos para pacotes com TV e telefone.",
            "- **Suporte 24/7:** Atendimento especializado a qualquer hora do dia.",
            "- **Instalação Gratuita:** Instalação rápida e sem custos adicionais."
        ],
        [
            "- **Novos Planos:** Confira nossos planos especiais para todas as necessidades.",
            "- **Planos Empresariais:** Soluções personalizadas para empresas de todos os tamanhos.",
            "- **Internet Fibra Óptica:** Velocidade e estabilidade incomparáveis."
        ],
        [
            "- **Promoção de Verão:** Descontos imperdíveis para aproveitar o calor!",
            "- **Pacote Premium:** Serviços adicionais exclusivos para assinantes.",
            "- **Oferta Limitada:** Aproveite enquanto durarem os estoques!"
        ]
    ]

    # Função para obter aleatoriamente um conjunto de promoções
    def get_random_promos(promos_sets):
        return random.choice(promos_sets)
    def update_promotions():
        selected_promos = get_random_promos(promos_sets)
        with col1:
            st.markdown('<div class="banner">', unsafe_allow_html=True)
            st.header("Promoções e Benefícios")
            for promo in selected_promos:
                st.write(promo)
            st.markdown('</div>', unsafe_allow_html=True)
    update_promotions()

    # Restante do código mantido como estava
    with col2:
        # Título centralizado estilizado
        st.markdown('<div class="title" style="font-family: Impact, Charcoal, sans-serif; font-size: 80px; font-style: italic; text-align: center;">BLUENETS</div>', unsafe_allow_html=True)
        st.markdown('<div class="container">', unsafe_allow_html=True)
        st.markdown('<div style="display: flex; justify-content: space-around;">', unsafe_allow_html=True)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;}</style>', unsafe_allow_html=True)
        options = ("Cadastro de Usuário", "Empresa", "Acesso")
        selected_tab = st.radio("Selecione o tipo de cadastro:", options, index=0, format_func=lambda x: x)
        st.markdown('</div>', unsafe_allow_html=True)

        # Exibir formulário correspondente à opção selecionada
        if selected_tab == "Cadastro de Usuário":
            st.markdown('<div class="custom-form">', unsafe_allow_html=True)
            st.header("Cadastro de Usuário")
            with st.form(key='usuario_form'):
                st.text_input("Nome Completo")
                st.text_input("CPF")
                st.text_input("Endereço Completo")
                st.text_input("Telefone")
                st.text_input("Email")
                submit_button = st.form_submit_button(label='Cadastrar', help="Clique para cadastrar seu usuário.")
                if submit_button:
                    st.success("Usuário cadastrado com sucesso!")
            st.markdown('</div>', unsafe_allow_html=True)

        elif selected_tab == "Empresa":
            st.markdown('<div class="custom-form">', unsafe_allow_html=True)
            st.header("Cadastro de Empresa")
            with st.form(key='empresa_form'):
                st.text_input("Nome da Empresa")
                st.text_input("CNPJ")
                st.text_input("Endereço da Empresa")
                st.text_input("Telefone da Empresa")
                st.text_input("Email da Empresa")
                submit_button = st.form_submit_button(label='Cadastrar', help="Clique para cadastrar a empresa.")
                if submit_button:
                    st.success("Empresa cadastrada com sucesso!")
            st.markdown('</div>', unsafe_allow_html=True)

        elif selected_tab == "Acesso":
            st.markdown('<div class="custom-form">', unsafe_allow_html=True)
            st.header("Cadastro de Acesso ao Site")
            with st.form(key='acesso_form'):
                st.text_input("Nome de Usuário")
                st.text_input("Senha", type="password")
                submit_button = st.form_submit_button(label='Cadastrar', help="Clique para cadastrar seu acesso.")
                if submit_button:
                    st.success("Acesso cadastrado com sucesso!")
            st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        # Banner com a imagem e título
        st.markdown('<div class="info-banner">', unsafe_allow_html=True)
        st.image("data/output/Design sem nome.png", use_column_width=True)  # Caminho para a imagem local
        st.header("NOSSA MISSÃO")
        st.markdown('</div>', unsafe_allow_html=True)

        # Texto informativo
        st.markdown('<div class="other-content">', unsafe_allow_html=True)
        st.write("""
        Aqui estão algumas informações sobre a missão da BLUENETS:

        - **Missão:** Fornecer acesso rápido e confiável à internet para todos os clientes.
        - **Visão:** Ser a operadora preferida pelos consumidores, oferecendo inovação e qualidade.
        - **Valores:** Compromisso com a excelência, integridade e responsabilidade social.

        Entre em contato conosco para mais detalhes e suporte!
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    # Rodapé
    st.markdown('<hr style="border-top: 5px solid #333;">', unsafe_allow_html=True)
    st.markdown('<div class="footer" style="position: fixed; bottom: 0; width: 100%; background-color: #f0f0f0; padding: 10px 20px; display: flex; justify-content: space-between; align-items: center; border-top: 2px solid #ffffff;">', unsafe_allow_html=True)

    # Texto de direitos autorais e Links
    st.markdown('''
    <div style="font-size: 15px; color: #ffffff;">
        © 2024 BLUENETS. Todos os direitos reservados. 
        <a href="#" style="color: #ffffff; text-decoration: none; margin-left: 15px;">Política de Privacidade</a> | 
        <a href="#" style="color: #ffffff; text-decoration: none; margin-left: 15px;">Termos de Uso</a> | 
        <a href="#" style="color: #ffffff; text-decoration: none; margin-left: 15px;">Contato</a>
    </div>
    ''', unsafe_allow_html=True)

    # Ícones sociais
    st.markdown('''
    <div style="font-size: 12px; color: #666;">
        <a href="https://facebook.com/bluenets" title="Bluenets Facebook"><img src="https://cdn2.downdetector.com/static/uploads/c/300/f0d8e/FB-f-Logo__blue_512.png" width="30" style="margin-right: 10px;"></a>
        <a href="https://twitter.com/bluenets" title="Bluenets Twitter"><img src="https://img.freepik.com/vetores-gratis/novo-design-de-icone-x-do-logotipo-do-twitter-em-2023_1017-45418.jpg?size=338&ext=jpg&ga=GA1.1.2113030492.1719619200&semt=ais_user" width="30" style="margin-right: 10px;"></a>
        <a href="https://www.instagram.com/bluenets" title="Bluenets Instagram"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/640px-Instagram_logo_2022.svg.png" width="30" style="margin-right: 10px;"></a>
        <a href="mailto:contato@bluenets.com" title="Contato Bluenets"><img src="https://lh5.googleusercontent.com/proxy/vRbr24c2MIh9IYindm11LYPnWB_ezakdeTeuoUbLb7qRj_stBvwkiLydcyftSq4166DRoFdYWtqrpPt6ieHb5YrIw47UxHcir9KeM5X2XRXzNX7F_-8jauGq6VcJCuVprpm_3v0_r3fPuUWrkQ" width="30" style="margin-right: 10px;"></a>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)







if __name__ == "__main__":
    main()
    customize_style()  # Personalização de estilo, se necessário
