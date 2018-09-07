FROM microsoft/dotnet:2.0-runtime AS base
WORKDIR /app

FROM microsoft/dotnet:2.0-sdk AS build
WORKDIR /src
COPY DotnetCoreConsole/DotnetCoreConsole.csproj DotnetCoreConsole/
RUN dotnet restore DotnetCoreConsole/DotnetCoreConsole.csproj
COPY . .
WORKDIR /src/DotnetCoreConsole
RUN dotnet build DotnetCoreConsole.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish DotnetCoreConsole.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["/bin/bash"]