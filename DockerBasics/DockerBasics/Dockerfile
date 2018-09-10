FROM microsoft/dotnet:2.0-runtime AS base
WORKDIR /app

FROM microsoft/dotnet:2.0-sdk AS build
WORKDIR /src
COPY DockerBasics/DockerBasics.csproj DockerBasics/
RUN dotnet restore DockerBasics/DockerBasics.csproj
COPY . .
WORKDIR /src/DockerBasics
RUN dotnet build DockerBasics.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish DockerBasics.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["/bin/bash"]
