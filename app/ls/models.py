from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Vegetables(models.Model):
    veg_type = models.CharField("Культура", max_length=50)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(upload_to='ls/images/%Y-%m-%d', blank=True)
    
    def __str__(self):
        return self.veg_type
    
    class Meta:
        verbose_name = 'Овощи'
        verbose_name_plural = 'Овощи'
    
class Tomato(models.Model):
    def get_default():
        return Vegetables.objects.get(veg_type="Томаты")
    
    t_id = models.ForeignKey(Vegetables, on_delete=models.CASCADE, verbose_name='Культура', default=get_default)
    veg_type = models.CharField("Культура", max_length=100, default = get_default)
    name = models.CharField("Сорт", max_length=500, default = 'Томат ')
    sorting = [
    ('Сорт', 'Сорт'),
    ('Гибрид', 'Гибрид'),
    ]
    sort = models.CharField("Сортность", max_length=50, choices=sorting, blank=True)
    vid = [
    ('Детерминантные', 'Детерминантные'),
    ('Индетерминантные', 'Индетерминантные'),
    ('Полудетерминантные', 'Полудетерминантные'),
    ('Штамбовые', 'Штамбовые'),
    ('Ампельные', 'Ампельные'),
    ]
    vids = models.CharField("Тип куста", max_length=50, choices=vid, blank=True)
    vids_image = models.CharField(max_length=100, default='ls/images/tomato/noimage.jpg')
    vids_description = models.TextField("Тип куста (описание)", blank=True)
    time = models.CharField("Срок созревания", max_length=50, blank=True)
    grunt = [
    ('Открытый грунт', 'Открытый грунт'),
    ('Закрытый грунт', 'Закрытый грунт'),
    ('Открытый и закрытый грунт', 'Открытый и закрытый грунт'),
    ]
    grunt_type = models.CharField("Способ выращивания", max_length=50, choices=grunt, blank=True)
    form = models.CharField("Форма плода", max_length=100, blank=True)
    size = models.CharField("Размер плода", max_length=50, blank=True)
    color = models.CharField("Цвет плода", max_length=50, blank=True)
    goal = models.CharField("Назначение", max_length=50, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(upload_to='ls/images/tomato', blank=True)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сорта томатов'
        verbose_name_plural = 'Сорта томатов'
        
    def clean(self):
        if self.vids == 'Детерминантные':
            self.vids_image = 'ls/images/tomato/determinantniy.jpg'
            self.vids_description = 'У томатов детерминантного типа куст перестает наращивать зеленую массу (стебли и листья) сразу после появления определенного количества цветочных кистей (в зависимости от сорта: от 2 до 6). Всю остальную часть периода вегетации растение «работает» исключительно на рост и созревание получившихся завязей. В результате количество плодов, созревающих на одном кусте, ограничено, но собрать их можно почти одновременно. Детерминантные сорта проще возделывать: они, как правило, образуют не высокие кусты (до 80-100 см), каждый из которых обходится без подвязки и не требует обширной площади питания. Такие томаты можно высаживать на небольших расстояниях друг от друга, экономя площадь участка и одновременно получая много однородных по спелости и другим потребительским качествам плодов. Томаты данного типа чаще всего выращивают в открытом грунте.'
        if self.vids == 'Индетерминантные':
            self.vids_image = 'ls/images/tomato/indeterminantniy.jpg'
            self.vids_description = 'Индетерминантные томаты развиваются иначе: они растут до тех пор, пока сохраняются оптимальные агротехнические условия (температура, влажность и т. д.), периодически формируя цветочные кисти. При этом процессы увеличения зеленой массы и «выкармливания» плодов протекают параллельно. Получается, что каждый куст при благоприятных условиях может вырасти в целое «дерево», но и количество плодов, которые он даст, ничем не ограничено. Зато растение нуждается в опоре, и урожай отдает постепенно: на каждом индетерминантном томате можно одновременно увидеть и цветущие кисти, и завязи, и плоды на разных стадиях созревания. В Сибири томаты такого типа лучше выращивать в теплицах, чтобы обеспечить растениям стабильно высокую температуру и влажность. Кусты должны располагаться подальше друг от друга, но и общее количество плодов, собранное с каждого из них за сезон, при хорошем уходе может получиться очень впечатляющим. Рекомендуем выращивать томаты этого типа в теплицах.'
        if self.vids == 'Полудетерминантные':
            self.vids_image = 'ls/images/tomato/poludeterminantniy.jpg'
            self.vids_description = 'Маша напишет про Полудетерминантные'
        if self.vids == 'Штамбовые':
            self.vids_image = 'ls/images/tomato/shtamboviy.jpg'
            self.vids_description = 'Маша напишет про Штамбовые'
        if self.vids == 'Ампельные':
            self.vids_image = 'ls/images/tomato/ampelniy.jpg'
            self.vids_description = 'Маша напишет про Ампельные'

class Perets(models.Model):
    def get_default():
        return Vegetables.objects.get(veg_type="Перцы")
    
    t_id = models.ForeignKey(Vegetables, on_delete=models.CASCADE, verbose_name='Культура', default=get_default)
    veg_type = models.CharField("Культура", max_length=100, default = get_default)
    name = models.CharField("Сорт", max_length=500, default = 'Перец ')
    vid = [
    ('Сладкие','Сладкие'),
    ('Острые','Острые'),
    ]
    vids = models.CharField("Вид перца", max_length=50, choices=vid, blank=True)
    vids_image = models.CharField(max_length=100, default='ls/images/perets/noimage.jpg')
    vids_description = models.TextField("Тип перцев (описание)", blank=True)
    sorting = [
    ('Сорт', 'Сорт'),
    ('Гибрид', 'Гибрид'),
    ]
    sort = models.CharField("Сортность", max_length=50, choices=sorting, blank=True)
    types = [
    ('Высокорослые', 'Высокорослые'),
    ('Низкорослые', 'Низкорослые'),
    ('Штамбовые', 'Штамбовые'),
    ]
    type_kusta = models.CharField("Тип куста", max_length=50, choices=types, blank=True)
    time = models.CharField("Срок созревания", max_length=50, blank=True)
    grunt = [
    ('Открытый грунт', 'Открытый грунт'),
    ('Закрытый грунт', 'Закрытый грунт'),
    ('Открытый и закрытый грунт', 'Открытый и закрытый грунт'),
    ('Временные укрытия', 'Временные укрытия'),
    ]
    grunt_type = models.CharField("Способ выращивания", max_length=50, choices=grunt, blank=True)
    form = models.CharField("Форма плода", max_length=50, blank=True)
    size = models.CharField("Размер плода", max_length=50, blank=True)
    color = models.CharField("Цвет плода", max_length=150, blank=True)
    goal = models.CharField("Назначение", max_length=50, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(upload_to='ls/images/perets', blank=True)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сорта перцев'
        verbose_name_plural = 'Сорта перцев'
        
    def clean(self):
        if self.vids == 'Сладкие':
            self.vids_image = 'ls/images/perets/sladkiy.jpg'
            self.vids_description = 'Очень сладенькие перчики'
        if self.vids == 'Острые':
            self.vids_image = 'ls/images/perets/ostriy.jpg'
            self.vids_description = 'Очень остренькие перчики'
        
class Baklajan(models.Model):
    def get_default():
        return Vegetables.objects.get(veg_type="Баклажаны")
    
    t_id = models.ForeignKey(Vegetables, on_delete=models.CASCADE, verbose_name='Культура', default=get_default)
    veg_type = models.CharField("Культура", max_length=100, default = get_default)
    vids = models.CharField("Тип куста", max_length=50, null=True)
    name = models.CharField("Сорт", max_length=500, default = 'Баклажан ')
    sorting = [
    ('Сорт', 'Сорт'),
    ('Гибрид', 'Гибрид'),
    ]
    sort = models.CharField("Сортность", max_length=50, choices=sorting, blank=True)
    types = [
    ('Высокорослый', 'ВМаша напишет про сладенькие перчикиысокорослый'),
    ('Низкорослый', 'Низкорослый'),
    ('Штамбовый', 'Штамбовый'),
    ]
    type_kusta = models.CharField("Тип куста", max_length=50, choices=types, blank=True)
    time = models.CharField("Срок созревания", max_length=50, blank=True)
    grunt = [
    ('Открытый грунт', 'Открытый грунт'),
    ('Закрытый грунт', 'Закрытый грунт'),
    ('Открытый и закрытый грунт', 'Открытый и закрытый грунт'),
    ('Временные укрытия', 'Временные укрытия'),
    ]
    grunt_type = models.CharField("Способ выращивания", max_length=50, choices=grunt, blank=True)
    form = models.CharField("Форма плода", max_length=100, blank=True)
    size = models.CharField("Размер плода", max_length=50, blank=True)
    color = models.CharField("Цвет плода", max_length=50, blank=True)
    goal = models.CharField("Назначение", max_length=50, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(upload_to='ls/images/baklajan', blank=True)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сорта баклажанов'
        verbose_name_plural = 'Сорта баклажанов'

class Kapusta(models.Model):
    def get_default():
        return Vegetables.objects.get(veg_type="Капуста")
    
    t_id = models.ForeignKey(Vegetables, on_delete=models.CASCADE, verbose_name='Культура', default=get_default)
    veg_type = models.CharField("Культура", max_length=100, default = get_default)
    name = models.CharField("Сорт", max_length=500, default = 'Капуста ')
    vid = [
    ('Белокочанная','Белокочанная'),
    ('Цветная','Цветная'),
    ('Брокколи','Брокколи'),
    ('Пекинская','Пекинская'),
    ('Кольраби','Кольраби'),
    ('Краснокочанная','Краснокочанная'),
    ('Савойская','Савойская'),
    ]
    vids = models.CharField("Вид капусты", max_length=50, choices=vid, blank=True)
    vids_image = models.CharField(max_length=100, default='ls/images/kapusta/noimage.jpg')
    vids_description = models.TextField("Вид капусты (описание)", blank=True)
    sorting = [
    ('Сорт', 'Сорт'),
    ('Гибрид', 'Гибрид'),
    ]
    sort = models.CharField("Сортность", max_length=50, choices=sorting, default='Гибрид')
    time = models.CharField("Срок созревания", max_length=50, blank=True)
    grunt = [
    ('Открытый грунт', 'Открытый грунт'),
    ('Закрытый грунт', 'Закрытый грунт'),
    ('Открытый и закрытый грунт', 'Открытый и закрытый грунт'),
    ('Временные укрытия', 'Временные укрытия'),
    ]
    grunt_type = models.CharField("Способ выращивания", max_length=50, choices=grunt, blank=True)
    form = models.CharField("Форма плода", max_length=50, blank=True)
    size = models.CharField("Размер плода", max_length=50, blank=True)
    color = models.CharField("Цвет плода", max_length=50, blank=True)
    massa = models.IntegerField(verbose_name="Масса плода", default=0)
    goal = models.CharField("Назначение", max_length=300, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(upload_to='ls/images/kapusta', blank=True)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сорта капусты'
        verbose_name_plural = 'Сорта капусты'
        
    def clean(self):
        if self.vids == 'Белокочанная':
            self.vids_image = 'ls/images/kapusta/belokochannaya.jpg'
            self.vids_description = 'Маша напишет про Белокочанная'
        if self.vids == 'Цветная':
            self.vids_image = 'ls/images/kapusta/tsvetnaya.jpg'
            self.vids_description = 'Маша напишет про Цветная'
        if self.vids == 'Брокколи':
            self.vids_image = 'ls/images/kapusta/brokkoli.jpg'
            self.vids_description = 'Маша напишет про Брокколи'
        if self.vids == 'Пекинская':
            self.vids_image = 'ls/images/kapusta/pekinskaya.jpg'
            self.vids_description = 'Маша напишет про Пекинская'
        if self.vids == 'Кольраби':
            self.vids_image = 'ls/images/kapusta/kolrabi.jpg'
            self.vids_description = 'Маша напишет про Кольраби'
        if self.vids == 'Краснокочанная':
            self.vids_image = 'ls/images/kapusta/krasnokachannaya.jpg'
            self.vids_description = 'Маша напишет про Краснокочанная'
        if self.vids == 'Савойская':
            self.vids_image = 'ls/images/kapusta/savoiskaya.jpg'
            self.vids_description = 'Маша напишет про Савойская'

class Svekla(models.Model):
    def get_default():
        return Vegetables.objects.get(veg_type="Свекла")
    
    t_id = models.ForeignKey(Vegetables, on_delete=models.CASCADE, verbose_name='Культура', default=get_default)
    veg_type = models.CharField("Культура", max_length=100, default = get_default)
    vids = models.CharField("Тип куста", max_length=50, null=True)
    name = models.CharField("Сорт", max_length=500, default = 'Свекла ')
    sorting = [
    ('Сорт', 'Сорт'),
    ('Гибрид', 'Гибрид'),
    ]
    sort = models.CharField("Сортность", max_length=50, choices=sorting, default='Гибрид')
    time = models.CharField("Срок созревания", max_length=50, blank=True)
    form = models.CharField("Форма плода", max_length=50, blank=True)
    size = models.CharField("Размер плода", max_length=50, blank=True)
    color = models.CharField("Цвет плода", max_length=50, blank=True)
    massa = models.IntegerField(verbose_name="Масса плода", default=0)
    goal = models.CharField("Назначение", max_length=50, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(upload_to='ls/images/svekla', blank=True)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сорта свеклы'
        verbose_name_plural = 'Сорта свеклы'
        
class Morkov(models.Model):
    def get_default():
        return Vegetables.objects.get(veg_type="Морковь")
    
    t_id = models.ForeignKey(Vegetables, on_delete=models.CASCADE, verbose_name='Культура', default=get_default)
    veg_type = models.CharField("Культура", max_length=100, default = get_default)
    vids = models.CharField("Тип куста", max_length=50, null=True)
    name = models.CharField("Сорт", max_length=500, default = 'Морковь ')
    sorting = [
    ('Сорт', 'Сорт'),
    ('Гибрид', 'Гибрид'),
    ]
    sort = models.CharField("Сортность", max_length=50, choices=sorting, default='Гибрид')
    sorting_type = [
    ('Берликум', 'Берликум'),
    ('Нантская', 'Нантская'),
    ('Шантане', 'Шантане'),
    ('Флакке', 'Флакке'),
    ]
    sort_type = models.CharField("Сортотип", max_length=50, choices=sorting_type, blank=True)
    time = models.CharField("Срок созревания", max_length=50, blank=True)
    form = models.CharField("Форма плода", max_length=50, blank=True)
    size = models.CharField("Размер плода", max_length=50, blank=True)
    color = models.CharField("Цвет плода", max_length=50, blank=True)
    massa = models.IntegerField(verbose_name="Масса плода", default=0)
    goal = models.CharField("Назначение", max_length=50, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(upload_to='ls/images/morkov', blank=True)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сорта моркови'
        verbose_name_plural = 'Сорта моркови'

class Redis(models.Model):
    def get_default():
        return Vegetables.objects.get(veg_type="Редис")
    
    t_id = models.ForeignKey(Vegetables, on_delete=models.CASCADE, verbose_name='Культура', default=get_default)
    veg_type = models.CharField("Культура", max_length=100, default = get_default)
    vids = models.CharField("Тип куста", max_length=50, null=True)
    name = models.CharField("Сорт", max_length=500, default = 'Редис ')
    sorting = [
    ('Сорт', 'Сорт'),
    ('Гибрид', 'Гибрид'),
    ]
    sort = models.CharField("Сортность", max_length=50, choices=sorting, default='Гибрид')
    time = models.CharField("Срок созревания", max_length=50, blank=True)
    form = models.CharField("Форма плода", max_length=50, blank=True)
    size = models.CharField("Размер плода", max_length=50, blank=True)
    color = models.CharField("Цвет плода", max_length=50, blank=True)
    massa = models.IntegerField(verbose_name="Масса плода", default=0)
    goal = models.CharField("Назначение", max_length=50, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(upload_to='ls/images/redis', blank=True)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сорта редиса'
        verbose_name_plural = 'Сорта редиса'

class Cucumber(models.Model):
    def get_default():
        return Vegetables.objects.get(veg_type="Огурцы")
    
    t_id = models.ForeignKey(Vegetables, on_delete=models.CASCADE, verbose_name='Культура', default=get_default)
    veg_type = models.CharField("Культура", max_length=100, default = get_default)
    name = models.CharField("Сорт", max_length=500, default = 'Огурец ')
    vid = [
    ('Пчелоопыляемый', 'Пчелоопыляемый'),
    ('Самоопыляемый', 'Самоопыляемый'),
    ('Партенокарпик', 'Партенокарпик'),
    ]
    #vids = models.CharField("Тип опыления", max_length=50, choices=vid, blank=True)
    #vids_image = models.CharField(max_length=100, default='ls/images/cucumber/noimage.jpg')
    #vids_description = models.TextField("Тип перцев (описание)", blank=True)
    vids = models.CharField("Тип", max_length=50, choices=vid, default='Самоопыляемый')
    #opylenie = models.CharField("Тип опыления", max_length=50, choices=vid, blank=True)
    sorting = [
    ('Сорт', 'Сорт'),
    ('Гибрид', 'Гибрид'),
    ]
    sort = models.CharField("Сортность", max_length=50, choices=sorting, default='Гибрид')
    time = models.CharField("Срок созревания", max_length=50, blank=True)
    form = models.CharField("Форма плода", max_length=50, blank=True)
    size_choice = [
    ('Короткоплодный', 'Короткоплодный'),
    ('Среднеплодный', 'Среднеплодный'),
    ('Длинноплодный', 'Длинноплодный'),
    ]
    size = models.CharField("Размер плода", max_length=50, choices=size_choice, blank=True)
    shkura_choice = [
    ('Гладкие', 'Гладкие'),
    ('Пупырчатые', 'Пупырчатые'),
    ]
    shkura = models.CharField("Поверхность", max_length=50, choices=shkura_choice, blank=True)
    color = models.CharField("Цвет плода", max_length=50, blank=True)
    massa = models.IntegerField(verbose_name="Масса плода", default=0)
    goal = models.CharField("Назначение", max_length=50, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(upload_to='ls/images/cucumber', blank=True)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сорта огурцов'
        verbose_name_plural = 'Сорта огурцов'
        
    #def clean(self):
        #if self.vids == 'Пчелоопыляемые':
            #self.vids_image = 'ls/images/cucumber/Pcheloopylyaemye.jpg'
            #self.vids_description = 'Маша напишет про Пчелоопыляемые'
        #if self.vids == 'Партенокарпики (самоопыляемые)':
            #self.vids_image = 'ls/images/cucumber/partenokarpiki.jpg'
            #self.vids_description = 'Маша напишет про Партенокарпики (самоопыляемые)'

class Flowers(models.Model):
    veg_type = models.CharField("Культура", max_length=100, default = 'Цветы')
    class_image = models.CharField("Фото категории", max_length=100, default = '/static/ls/images/flowers_all.jpg')
    vids = models.CharField("Вид", max_length=500, default = '')
    vid_image = models.CharField("Фото вида", max_length=100, default = '')
    vid_descr = models.CharField("Описание вида", max_length=100, blank=True)
    name = models.CharField("Сорт", max_length=500, default = '')
    lifetime = models.CharField("Время жизни", max_length=50, blank=True)
    height = models.CharField("Высота", max_length=50, default = ' см', blank=True)
    sozvetie = models.CharField("Соцветие", max_length=50, default = ' см', blank=True)
    tsvetok = models.CharField("Цветок", max_length=50, default = ' см', blank=True)
    color = models.CharField("Цвет", max_length=50, default = '', blank=True)
    dlinapobegov = models.CharField("Длина побегов", max_length=50, default = ' см', blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(upload_to='ls/images/flowers/%Y-%m-%d', blank=True)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    
    def clean(self):
        if self.vids == 'Астра':
            self.vid_image = 'ls/images/flowers/astra.jpg'
            self.vid_descr = 'Для первоклашек'
        elif self.vids == 'Арабис':
            self.vid_image = 'ls/images/flowers/arabis.jpg'
            self.vid_descr = 'Непонятно что для газона.. но красиво'
        elif self.vids == 'Аренария':
            self.vid_image = 'ls/images/flowers/arenaria.jpg'
            self.vid_descr = 'Аренария'
        elif self.vids == 'Армерия':
            self.vid_image = 'ls/images/flowers/armeria.jpg'
            self.vid_descr = 'Армерия???'
        elif self.vids == 'Аубреция':
            self.vid_image = 'ls/images/flowers/aubretsia.jpg'
            self.vid_descr = 'Аубреция???'
        else:
            self.vid_image = 'ls/images/noimage.jpg'
            
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Цветы'
        verbose_name_plural = 'Цветы'


class Comments(models.Model):
    toSortName = models.CharField("Сорт", max_length=500)
    authorName = models.CharField("Имя", max_length=50)
    authorEmail = models.EmailField("Email", max_length=50)
    comment = models.TextField("Комментарий")
    approved = models.BooleanField("Одобрено", default = False)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    
    class Meta:
        verbose_name = 'Комментарии и отзывы'
        verbose_name_plural = 'Комментарии и отзывы'
        
    def __str__(self):
        return self.authorName + ' email: ' + self.authorEmail + ' комментарий к ' +self.toSortName+ ' '+self.pub_date.strftime('%Y-%m-%d %H:%M')
