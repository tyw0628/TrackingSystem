# Generated by Django 2.2.6 on 2019-11-27 00:01

import KumoGT.crypt_fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deg_type', models.CharField(choices=[('phd', 'PhD'), ('ms_thesis', 'MS(Thesis)'), ('ms_non_thesis', 'MS(Non-Thesis)'), ('meng', 'MEng')], default='none', max_length=63)),
                ('major', models.CharField(choices=[('cpsc', 'CPSC'), ('cecn', 'CECN'), ('en', 'EN'), ('comp', 'COMP')], max_length=63, verbose_name='Major')),
                ('first_reg_year', models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(32767), django.core.validators.MinValueValidator(-32768)], verbose_name='First Registered Year')),
                ('first_reg_sem', models.CharField(choices=[('fall', 'Fall'), ('spring', 'Spring'), ('summer', 'Summer')], default='fall', max_length=31, verbose_name='First Registered Semester')),
                ('last_reg_year', models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(32767), django.core.validators.MinValueValidator(-32768)], verbose_name='Last Registered Year')),
                ('last_reg_sem', models.CharField(choices=[('fall', 'Fall'), ('spring', 'Spring'), ('summer', 'Summer')], default='fall', max_length=31, verbose_name='Last Registered Semester')),
                ('deg_recv_year', models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(32767), django.core.validators.MinValueValidator(-32768)], verbose_name='Degree Received Year')),
                ('deg_recv_sem', models.CharField(choices=[('fall', 'Fall'), ('spring', 'Spring'), ('summer', 'Summer')], default='fall', max_length=31, verbose_name='Degree Received Semester')),
            ],
        ),
        migrations.CreateModel(
            name='T_D_Prop_Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', KumoGT.crypt_fields.EncryptedFileField(upload_to='documents/', verbose_name='Document')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('appr_cs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved CS')),
                ('appr_ogs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved OGS')),
                ('notes', models.CharField(blank=True, max_length=511, verbose_name='Notes')),
                ('doc_type', models.CharField(choices=[('not_sel', 'Not Selected'), ('title_page', 'Thesis/Dissertation Proposal Title Page'), ('prop', 'Thesis/Dissertation Proposal')], default='not_sel', max_length=255)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='T_D_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('url', models.URLField()),
                ('degree', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
        ),
        migrations.CreateModel(
            name='T_D_Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', KumoGT.crypt_fields.EncryptedFileField(upload_to='documents/', verbose_name='Document')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('appr_cs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved CS')),
                ('appr_ogs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved OGS')),
                ('notes', models.CharField(blank=True, max_length=511, verbose_name='Notes')),
                ('doc_type', models.CharField(choices=[('not_sel', 'Not Selected'), ('approval', 'Thesis/Dissertation Approval Page'), ('t_d', 'Thesis/Dissertation')], default='not_sel', max_length=255)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uin', models.CharField(max_length=63, unique=True, verbose_name='UIN')),
                ('first_name', models.CharField(max_length=127, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=127, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=127, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('not_ans', 'Prefer Not to Answer'), ('male', 'Male'), ('female', 'Female'), ('trans', 'Transgender')], default='not_ans', max_length=63, verbose_name='Gender')),
                ('ethnicity', models.CharField(choices=[('unknown', 'Unknown'), ('african_ame', 'Black/African American'), ('asian', 'Asian'), ('white', 'White'), ('his_or_la', 'Hispanic or Latino'), ('island', 'Native Hawaiian or Pacific Islander'), ('international', 'International'), ('not_ans', 'Prefer Not to Answer')], default='unknown', max_length=63, verbose_name='Ethnicity')),
                ('us_residency', models.CharField(choices=[('usa', 'USA'), ('usc', 'USC - U.S. Citizen'), ('usfr', 'USPR - U.S. Permanent Resident'), ('nra', 'NRA - Non Resident Alien / International'), ('u', 'U - Unknown')], default='u', max_length=63, verbose_name='US Residency')),
                ('texas_residency', models.CharField(choices=[('r', 'R - Resident'), ('t', 'T - Resident, Not State Funded'), ('u', 'U - Resident, Not State Funded, 7 Year'), ('n', 'N - Non-Resident'), ('p', 'P - Non-Resident, Not State Funded, 7 Year'), ('i', 'I - International'), ('k', 'K - International, Not State Funded, 7 Year'), ('j', 'J - International, Not State Funded'), ('w', 'W - SB1502, Not State Funded, 7 Year'), ('v', 'V - SB1520, Not State Funded'), ('h', 'H - SZASSTD'), ('s', 'S - Unknown')], default='u', max_length=63, verbose_name='Texas Residency')),
                ('citizenship', models.CharField(choices=[('AW', 'Aruba'), ('AF', 'Islamic Republic of Afghanistan'), ('AO', 'Republic of Angola'), ('AI', 'Anguilla'), ('AX', 'Åland Islands'), ('AL', 'Republic of Albania'), ('AD', 'Principality of Andorra'), ('AE', 'United Arab Emirates'), ('AR', 'Argentine Republic'), ('AM', 'Republic of Armenia'), ('AS', 'American Samoa'), ('AQ', 'Antarctica'), ('TF', 'French Southern Territories'), ('AG', 'Antigua and Barbuda'), ('AU', 'Australia'), ('AT', 'Republic of Austria'), ('AZ', 'Republic of Azerbaijan'), ('BI', 'Republic of Burundi'), ('BE', 'Kingdom of Belgium'), ('BJ', 'Republic of Benin'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BF', 'Burkina Faso'), ('BD', "People's Republic of Bangladesh"), ('BG', 'Republic of Bulgaria'), ('BH', 'Kingdom of Bahrain'), ('BS', 'Commonwealth of the Bahamas'), ('BA', 'Republic of Bosnia and Herzegovina'), ('BL', 'Saint Barthélemy'), ('BY', 'Republic of Belarus'), ('BZ', 'Belize'), ('BM', 'Bermuda'), ('BO', 'Plurinational State of Bolivia'), ('BR', 'Federative Republic of Brazil'), ('BB', 'Barbados'), ('BN', 'Brunei Darussalam'), ('BT', 'Kingdom of Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Republic of Botswana'), ('CF', 'Central African Republic'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'), ('CH', 'Swiss Confederation'), ('CL', 'Republic of Chile'), ('CN', "People's Republic of China"), ('CI', "Republic of Côte d'Ivoire"), ('CM', 'Republic of Cameroon'), ('CD', 'Congo, The Democratic Republic of the'), ('CG', 'Republic of the Congo'), ('CK', 'Cook Islands'), ('CO', 'Republic of Colombia'), ('KM', 'Union of the Comoros'), ('CV', 'Republic of Cabo Verde'), ('CR', 'Republic of Costa Rica'), ('CU', 'Republic of Cuba'), ('CW', 'Curaçao'), ('CX', 'Christmas Island'), ('KY', 'Cayman Islands'), ('CY', 'Republic of Cyprus'), ('CZ', 'Czech Republic'), ('DE', 'Federal Republic of Germany'), ('DJ', 'Republic of Djibouti'), ('DM', 'Commonwealth of Dominica'), ('DK', 'Kingdom of Denmark'), ('DO', 'Dominican Republic'), ('DZ', "People's Democratic Republic of Algeria"), ('EC', 'Republic of Ecuador'), ('EG', 'Arab Republic of Egypt'), ('ER', 'the State of Eritrea'), ('EH', 'Western Sahara'), ('ES', 'Kingdom of Spain'), ('EE', 'Republic of Estonia'), ('ET', 'Federal Democratic Republic of Ethiopia'), ('FI', 'Republic of Finland'), ('FJ', 'Republic of Fiji'), ('FK', 'Falkland Islands (Malvinas)'), ('FR', 'French Republic'), ('FO', 'Faroe Islands'), ('FM', 'Federated States of Micronesia'), ('GA', 'Gabonese Republic'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('GE', 'Georgia'), ('GG', 'Guernsey'), ('GH', 'Republic of Ghana'), ('GI', 'Gibraltar'), ('GN', 'Republic of Guinea'), ('GP', 'Guadeloupe'), ('GM', 'Republic of the Gambia'), ('GW', 'Republic of Guinea-Bissau'), ('GQ', 'Republic of Equatorial Guinea'), ('GR', 'Hellenic Republic'), ('GD', 'Grenada'), ('GL', 'Greenland'), ('GT', 'Republic of Guatemala'), ('GF', 'French Guiana'), ('GU', 'Guam'), ('GY', 'Republic of Guyana'), ('HK', 'Hong Kong Special Administrative Region of China'), ('HM', 'Heard Island and McDonald Islands'), ('HN', 'Republic of Honduras'), ('HR', 'Republic of Croatia'), ('HT', 'Republic of Haiti'), ('HU', 'Hungary'), ('ID', 'Republic of Indonesia'), ('IM', 'Isle of Man'), ('IN', 'Republic of India'), ('IO', 'British Indian Ocean Territory'), ('IE', 'Ireland'), ('IR', 'Islamic Republic of Iran'), ('IQ', 'Republic of Iraq'), ('IS', 'Republic of Iceland'), ('IL', 'State of Israel'), ('IT', 'Italian Republic'), ('JM', 'Jamaica'), ('JE', 'Jersey'), ('JO', 'Hashemite Kingdom of Jordan'), ('JP', 'Japan'), ('KZ', 'Republic of Kazakhstan'), ('KE', 'Republic of Kenya'), ('KG', 'Kyrgyz Republic'), ('KH', 'Kingdom of Cambodia'), ('KI', 'Republic of Kiribati'), ('KN', 'Saint Kitts and Nevis'), ('KR', 'Korea, Republic of'), ('KW', 'State of Kuwait'), ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanese Republic'), ('LR', 'Republic of Liberia'), ('LY', 'Libya'), ('LC', 'Saint Lucia'), ('LI', 'Principality of Liechtenstein'), ('LK', 'Democratic Socialist Republic of Sri Lanka'), ('LS', 'Kingdom of Lesotho'), ('LT', 'Republic of Lithuania'), ('LU', 'Grand Duchy of Luxembourg'), ('LV', 'Republic of Latvia'), ('MO', 'Macao Special Administrative Region of China'), ('MF', 'Saint Martin (French part)'), ('MA', 'Kingdom of Morocco'), ('MC', 'Principality of Monaco'), ('MD', 'Republic of Moldova'), ('MG', 'Republic of Madagascar'), ('MV', 'Republic of Maldives'), ('MX', 'United Mexican States'), ('MH', 'Republic of the Marshall Islands'), ('MK', 'Republic of North Macedonia'), ('ML', 'Republic of Mali'), ('MT', 'Republic of Malta'), ('MM', 'Republic of Myanmar'), ('ME', 'Montenegro'), ('MN', 'Mongolia'), ('MP', 'Commonwealth of the Northern Mariana Islands'), ('MZ', 'Republic of Mozambique'), ('MR', 'Islamic Republic of Mauritania'), ('MS', 'Montserrat'), ('MQ', 'Martinique'), ('MU', 'Republic of Mauritius'), ('MW', 'Republic of Malawi'), ('MY', 'Malaysia'), ('YT', 'Mayotte'), ('NA', 'Republic of Namibia'), ('NC', 'New Caledonia'), ('NE', 'Republic of the Niger'), ('NF', 'Norfolk Island'), ('NG', 'Federal Republic of Nigeria'), ('NI', 'Republic of Nicaragua'), ('NU', 'Niue'), ('NL', 'Kingdom of the Netherlands'), ('NO', 'Kingdom of Norway'), ('NP', 'Federal Democratic Republic of Nepal'), ('NR', 'Republic of Nauru'), ('NZ', 'New Zealand'), ('OM', 'Sultanate of Oman'), ('PK', 'Islamic Republic of Pakistan'), ('PA', 'Republic of Panama'), ('PN', 'Pitcairn'), ('PE', 'Republic of Peru'), ('PH', 'Republic of the Philippines'), ('PW', 'Republic of Palau'), ('PG', 'Independent State of Papua New Guinea'), ('PL', 'Republic of Poland'), ('PR', 'Puerto Rico'), ('KP', "Democratic People's Republic of Korea"), ('PT', 'Portuguese Republic'), ('PY', 'Republic of Paraguay'), ('PS', 'the State of Palestine'), ('PF', 'French Polynesia'), ('QA', 'State of Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwandese Republic'), ('SA', 'Kingdom of Saudi Arabia'), ('SD', 'Republic of the Sudan'), ('SN', 'Republic of Senegal'), ('SG', 'Republic of Singapore'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJ', 'Svalbard and Jan Mayen'), ('SB', 'Solomon Islands'), ('SL', 'Republic of Sierra Leone'), ('SV', 'Republic of El Salvador'), ('SM', 'Republic of San Marino'), ('SO', 'Federal Republic of Somalia'), ('PM', 'Saint Pierre and Miquelon'), ('RS', 'Republic of Serbia'), ('SS', 'Republic of South Sudan'), ('ST', 'Democratic Republic of Sao Tome and Principe'), ('SR', 'Republic of Suriname'), ('SK', 'Slovak Republic'), ('SI', 'Republic of Slovenia'), ('SE', 'Kingdom of Sweden'), ('SZ', 'Kingdom of Eswatini'), ('SX', 'Sint Maarten (Dutch part)'), ('SC', 'Republic of Seychelles'), ('SY', 'Syrian Arab Republic'), ('TC', 'Turks and Caicos Islands'), ('TD', 'Republic of Chad'), ('TG', 'Togolese Republic'), ('TH', 'Kingdom of Thailand'), ('TJ', 'Republic of Tajikistan'), ('TK', 'Tokelau'), ('TM', 'Turkmenistan'), ('TL', 'Democratic Republic of Timor-Leste'), ('TO', 'Kingdom of Tonga'), ('TT', 'Republic of Trinidad and Tobago'), ('TN', 'Republic of Tunisia'), ('TR', 'Republic of Turkey'), ('TV', 'Tuvalu'), ('TW', 'Taiwan, Province of China'), ('TZ', 'United Republic of Tanzania'), ('UG', 'Republic of Uganda'), ('UA', 'Ukraine'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Eastern Republic of Uruguay'), ('US', 'United States of America'), ('UZ', 'Republic of Uzbekistan'), ('VA', 'Holy See (Vatican City State)'), ('VC', 'Saint Vincent and the Grenadines'), ('VE', 'Bolivarian Republic of Venezuela'), ('VG', 'British Virgin Islands'), ('VI', 'Virgin Islands of the United States'), ('VN', 'Socialist Republic of Viet Nam'), ('VU', 'Republic of Vanuatu'), ('WF', 'Wallis and Futuna'), ('WS', 'Independent State of Samoa'), ('YE', 'Republic of Yemen'), ('ZA', 'Republic of South Africa'), ('ZM', 'Republic of Zambia'), ('ZW', 'Republic of Zimbabwe')], max_length=127, verbose_name='Citizenship')),
                ('status', models.CharField(choices=[('current', 'Current'), ('graduated', 'Gradudated'), ('invalid', 'Invalid')], default='current', max_length=63, verbose_name='Status')),
                ('start_year', models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(32767), django.core.validators.MinValueValidator(-32768)], verbose_name='Start Year')),
                ('start_sem', models.CharField(choices=[('fall', 'Fall'), ('spring', 'Spring'), ('summer', 'Summer')], default='fall', max_length=31, verbose_name='Start Semester')),
                ('advisor', models.CharField(blank=True, max_length=511, verbose_name='Advisor')),
                ('upe', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=15, verbose_name='UPE')),
                ('ace', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=15, verbose_name='ACE')),
                ('iga', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=15, verbose_name='IGA')),
                ('cur_degree', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='KumoGT.Degree', verbose_name='Current Degree')),
            ],
        ),
        migrations.CreateModel(
            name='Session_Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('note', models.CharField(blank=True, max_length=4096)),
                ('stu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Student', verbose_name='Student')),
            ],
        ),
        migrations.CreateModel(
            name='Pre_Exam_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Prelim Date')),
                ('result', models.CharField(choices=[('none', '----'), ('pass', 'Pass'), ('fail', 'Fail')], default='none', max_length=15)),
                ('degree', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
        ),
        migrations.CreateModel(
            name='Pre_Exam_Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', KumoGT.crypt_fields.EncryptedFileField(upload_to='documents/', verbose_name='Document')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('appr_cs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved CS')),
                ('appr_ogs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved OGS')),
                ('notes', models.CharField(blank=True, max_length=511, verbose_name='Notes')),
                ('doc_type', models.CharField(choices=[('not_sel', 'Not Selected'), ('checklist', 'Preliminary Exam Checklist'), ('report', 'Preliminary Exam Report'), ('written', 'Preliminary Exam Written')], default='not_sel', max_length=255)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fin_Exam_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('result', models.CharField(choices=[('none', '----'), ('pass', 'Pass'), ('fail', 'Fail')], default='none', max_length=15)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('room', models.CharField(blank=True, max_length=255)),
                ('abstract', models.CharField(blank=True, max_length=1023)),
                ('degree', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Exam_Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', KumoGT.crypt_fields.EncryptedFileField(upload_to='documents/', verbose_name='Document')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('appr_cs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved CS')),
                ('appr_ogs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved OGS')),
                ('notes', models.CharField(blank=True, max_length=511, verbose_name='Notes')),
                ('doc_type', models.CharField(choices=[('not_sel', 'Not Selected'), ('request', 'Request for Final Examination'), ('req_for_exemp', 'Request for exemption from Final Examination'), ('report', 'Report of Final Exam')], default='not_sel', max_length=255)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='degree',
            name='stu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Student', verbose_name='Student'),
        ),
        migrations.CreateModel(
            name='Deg_Plan_Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', KumoGT.crypt_fields.EncryptedFileField(upload_to='documents/', verbose_name='Document')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('appr_cs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved CS')),
                ('appr_ogs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved OGS')),
                ('notes', models.CharField(blank=True, max_length=511, verbose_name='Notes')),
                ('doc_type', models.CharField(choices=[('not_sel', 'Not Selected'), ('deg_plan', 'Degree Plan'), ('P_change_commitee', 'Petition for change of committee'), ('P_course_change', 'Petition for course change'), ('P_extension_of_time_limits', 'Petition for extension of time limits'), ('P_waivers_of_exceptions', 'Petition for waivers of exceptions'), ('mdd', 'MDD'), ('other', 'Other')], default='not_sel', max_length=255)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
