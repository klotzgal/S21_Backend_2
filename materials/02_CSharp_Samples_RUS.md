#### **C#**
Для написания HTTP API на C# используется фреймворк ASP.NET. Давай сначала рассмотрим, что такое модели и контроллеры.

**Модель** - некоторая формализация понятия, которое используется в системе. Модель несёт в себе данные в виде атрибутов, при этом модель никак не связана с UI. За данные модель отвечает самостоятельно (проводит валидацию).

```csharp
public abstract class BaseModel
{
    public Guid Id { get; set; }
}
```

```csharp
public class ExampleModel : BaseModel
{
    public string ExampleModelAttr { get; set; }
}
```

**Репозитории** используются для работы с Базами Данных (см. паттерн "Репозиторий"). На уровне репозитория реализуются CRUD операции над данными (CREATE, READ, UPDATE, DELETE).

```csharp
public interface IExampleRepository
{
    public Task<List<ExampleModel>> GetAllExampleModelsAsync();

    public Task CreateExampleModelAsync(Guid id, string exampleModelAttr);

    ...
}
```

```csharp
public class ExampleRepository : IExampleRepository
{
    // реализация интерфейса
    ...
}
```

**Сервисы** используются для реализации бизнес-логики приложений.

```csharp
public interface IExampleService
{
    public Task DoExampleBusiness();
}
```

```csharp
public class ExampleService : IExampleService
{
    private readonly IExampleRepository _exampleRepository { get; set; }

    ...
    
    public Task DoExampleBusiness()
    {
        // реализация бизнес-логики
        ...
    }
}
```

Проектировать систему рекомендуется соблюдая принципы SOLID. Кроме того, на уровне фреймворка реализован паттерн Dependency Injection, позволяющий "прокидывать" зависимости в компоненты системы.

**Контроллер** - посредник между бизнес-логикой и клиентской частью приложения. Контроллер обрабатывает запросы по сети, события от пользователей, отвечает за обновление данных и является точкой входа в обработку запроса.

```csharp
[ApiController]
[Route("api/example")]
public class ExampleController : ControllerBase
{
    private readonly IExampleService _exampleService;

    // Dependency injection
    public ExampleController(IExampleService exampleService)
    {
        _exampleService = exampleService;
    }

    [HttpPost]
    public async Task<IActionResult> DoBusiness()
    {
        _exampleService.DoExampleBusiness();
        return Ok();
    }
}
```