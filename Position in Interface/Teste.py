from ModulosCTK import *

Janela = CriarJanelaP("Aula Stick", "600x600+500+50", 1)
texto1 = CriarLabel(Janela, "Nome", 1, 1)
caixa1 = CriarCaixaTexto(Janela, 200, 30, 2, 1, "Digite o nome")
botao1 = CriarBotao(Janela, "Enviar", "clique", 100, 30, 3, 1)

Janela.mainloop()