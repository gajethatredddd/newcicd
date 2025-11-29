pipeline
{
    agent
any

stages
{
    stage('Build')
{
    steps
{
    sh
'docker-compose build'
}
}

stage('Test')
{
    steps
{
    echo
'Тесты пропущены, всё чётко! ✅'
}
}

stage('Deploy')
{
    steps
{
    sh
'docker-compose down'
sh
'docker-compose up -d'
}
}
}

post
{
    always
{
    echo
'Пайплайн завершен!'
}
}
}