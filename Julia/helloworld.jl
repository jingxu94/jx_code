print("Hello World, Julia!\n")
# print(typeof(y),"\n")
# print(typeof(3000000000000))
for T = [Int8,Int16,Int32,Int64,Int128,UInt8,UInt16,UInt32,UInt64,UInt128]
    println("$(lpad(T,7)): [$(typemin(T)),$(typemax(T))]")
end
println(typemin(Int32),"\n",typemax(Int32))

x = typemax(Int64)
x += 1
println(x)
println(x==typemin(Int64),"\n")

println(isequal(x,typemin(Int64)))
println(isfinite(x))
println(isinf(x))
println(isnan(x))

function f(x,y)
    x+y
end
println(f(2,3))