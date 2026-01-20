1type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
23function argumentsLength(...args: JSONValue[]): number {
4    return args.length
5};
67/**
89