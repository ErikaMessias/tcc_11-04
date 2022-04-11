# Generated by Django 4.0.3 on 2022-04-05 00:14

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentralTrab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCentralTrab', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='centroCusto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoCentro', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='contaRazao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeContaRazao', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='divisao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDivisao', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='localInstal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeLocalInstal', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='nivelAcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeAcesso', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='prioridade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomePrioridade', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProduto', models.CharField(max_length=20)),
                ('partNumber', models.IntegerField()),
                ('CentroCusto', models.CharField(max_length=4)),
                ('descri', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeResponsavel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tipoAtv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nometipoAtv', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tipoMovimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nometipoMovimento', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tipoOrdem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeTipoOrdem', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edv', models.BigIntegerField()),
                ('senha', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=80)),
                ('idUserFK', models.BigIntegerField(blank=True, null=True)),
                ('idNivelAcessFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.nivelacesso')),
                ('idRespFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.responsavel')),
            ],
        ),
        migrations.CreateModel(
            name='TransacaoSucata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=100)),
                ('txtBreve', models.CharField(max_length=20)),
                ('trab', models.DecimalField(decimal_places=2, max_digits=5)),
                ('un', models.CharField(blank=True, default='H', max_length=2, null=True)),
                ('idCenTrabFK', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CentralTrab', to='home.centraltrab')),
                ('idCentroCustoFK', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='centroCusto', to='home.centrocusto')),
                ('idLocalFK', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='localInstal', to='home.localinstal')),
                ('idPrioridadeFK', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prioridade', to='home.prioridade')),
                ('iddivisaoFK', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='divisao', to='home.divisao')),
                ('idtipoOrdemFK', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_ordem', to='home.tipoordem')),
                ('idtipoavtFK', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipoAtv', to='home.tipoatv')),
            ],
        ),
        migrations.CreateModel(
            name='TransacaoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recebedor', models.CharField(max_length=15)),
                ('material', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField()),
                ('umr', models.CharField(max_length=10)),
                ('dep', models.CharField(max_length=10)),
                ('idCentroCFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.centrocusto')),
                ('idContaRazaoFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.contarazao')),
                ('idProdutoFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.produto')),
                ('idTipoMovimentoFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.tipomovimento')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoSucata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('idTransSucataFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.transacaosucata')),
                ('idUsuarioFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('idTraProdutoFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.transacaoproduto')),
                ('idUsuarioFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=home.models.upload_image_produto)),
                ('idProdutoFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produto', to='home.produto')),
            ],
        ),
    ]
