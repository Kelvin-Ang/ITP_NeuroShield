#include <iosteam>
#include <functional>

int main()
{
	[out = std::ref(std::cout << "Hello")](){ out.get() << "World\n"}();
}
