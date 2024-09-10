#subir projeto
dentro de mysite
python .\manage.py runserver


#cria o arquivo na pasta de controle de banco de dados
python manage.py makemigrations
#aplica o pacote no banco de dados
python .\manage.py migrate
#retornando pacotes do migrate, digita-se o comando abaixo com a versão especifica e depois se deleta o arquivo, para não ser excluido novamente
python .\manage.py migrate polls 0002


#git 
git add .
git commit -m 'feat-add field'
git push -u origin master


#consulta banco de dados
python .\manage.py shell -i ipyton