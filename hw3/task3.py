def ten_popular(text: str) -> list[str]:
    delete = ".,!?;:-[]{}()='"
    for i in delete:
        text = text.replace(i, "")
    text = text.lower()
    return sorted(set(text.split()), key=lambda x: text.count(x))[-10:]

text = "C++ широко используется для разработки программного обеспечения, являясь одним из самых популярных языков программирования[мнения 1][мнения 2]. Область его применения включает создание операционных систем, разнообразных прикладных программ, драйверов устройств, приложений для встраиваемых систем, высокопроизводительных серверов, а также компьютерных игр. Существует множество реализаций языка C++, как бесплатных, так и коммерческих и для различных платформ. Например, на платформе x86 это GCC, Clang, Visual C++, Intel C++ Compiler, Embarcadero (Borland) C++ Builder и другие. C++ оказал огромное влияние на другие языки программирования, в первую очередь на Java и C#."
text=ten_popular(text)
print(text)