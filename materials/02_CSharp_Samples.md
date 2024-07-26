#### **C#**
The ASP.NET framework is used to write the HTTP API in C#. Let's first look at models and controllers.
A **Model** is some formalization of a concept that is used in the system. The model contains data in the form of attributes, and the model is in no way connected to the UI. The model is responsible for the data on its own (it performs validation).

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

**Repositories** are used to work with databases (see Repository pattern). The repository level implements CRUD operations on data (CREATE, READ, UPDATE, DELETE).

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
    // interface implementation
    ...
}
```

**Services** are used to implement application business logic.

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
        // business logic implementation
        ...
    }
}
```

It is recommended to design the system following SOLID principles. In addition, the Dependency Injection pattern is implemented at the framework level, which allows you to "inject" dependencies to system components.

**Controller** is an intermediary between the business logic and the client side of the application. The controller handles network requests, user events, is responsible for updating data, and is the entry point into request processing.

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