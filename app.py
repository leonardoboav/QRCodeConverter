#Importação de biblioteca
import qrcode

#Converte a URL desejável em qrcode 
imagem = qrcode.make("https://www.youtube.com.br/")

#Salvar o qrcode (jpg, png, pdf, etc)
imagem.save("primeiro_qrcode.jpg")

print(imagem)

