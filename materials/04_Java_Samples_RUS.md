#### **Java**
Создание приложения HTTP API в Java начинается так же с описания моделей. Будем использовать библиотеку Spring Boot.

```java
public class ExampleModel {
    private Integer id;
    private String exampleModelAttr;

    public Integer getId() {
       return id;
    }

    public void setId(Integer id) {
       this.id = id;
    }

    public String getExampleModelAttr() {
       return id;
    }

    public void setExampleModelAttr(String id) {
       this.id = id;
    }
}
```

Теперь опишем интерфейс и его реализацию - сервис.

```java
public interface ExampleService {
    void create(ExampleModel model);
    void DoExampleBusiness();
}
```

```java
@Service
public class ExampleServiceImpl implements ExampleService {
    private static final ExampleRepository  exampleRepository = new ExampleRepositoryImpl();
    private static final AtomicInteger modelIdHolder = new AtomicInteger();

    @Override
    public void create(ExampleModel model) {
        final int modelId = modelIdHolder.incrementAndGet();
        model.setId(modelId);
        exampleRepository.create(model);
    }

    @Override
    public void DoExampleBusiness() {
        // Business logic
    }
}
```

Теперь давай напишем контроллер.

```java
@RestController
public class ExampleController {
    private final ExampleService exampleService;

    @Autowired
    public ExampleController(ExampleService exampleService) {
        this.exampleService = exampleService;
    }
}
```

Autowired указывает на то, что используется внедрение зависимостей (Dependency Injection).

Теперь напишем методы контроллера.

```java
@PostMapping(value = "/model")
public ReponseEntity<?> create(@RequestBody ExampleModel model) {
    exampleService.create(model);
    return new ReponseEntity<>(HttpStatus.CREATED);
}
```

PostMapping указывает на то, что по адресу /model можно послать POST-запрос, который будет обработан данным методом.