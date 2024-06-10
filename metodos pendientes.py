metodos pendientes

@login_required
def libros_listar(request):
    libros = Libro.objects.filter(eliminado = False)
    return render(request, "sitio1/libros/libros.html",{'datos':libros})

def libros_eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.eliminado = True
    libro.save()
    return redirect("/libros/listar")

def libros_editar(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == "GET":
        form = NuevoLibro(instance=libro)
        return render(request, 'sitio1/libros/libros_formulario.html', {'libro':libro, 'form':form})
    else:
        form = NuevoLibro(request.POST, instance=libro)
        form.save()
        return redirect("/libros/listar")

def libros_agregar(request):
    if request.method == 'GET':
        return render(request, "sitio1/libros/libros_agregar.html",{'form': NuevoLibro()})
    else:
        eliminado = request.POST.get('eliminado')
        if eliminado == 'on':
            eliminado = True
        else:
            eliminado = False

        Libro.objects.create(
            titulo = request.POST['titulo'],
            nombre_autor = request.POST['nombre_autor'], 
            categoria = request.POST['categoria'], 
            descripcion = request.POST['descripcion'], 
            precio = request.POST['precio'],
            fecha_ingreso = request.POST['fecha_ingreso'],
            eliminado = eliminado
        )
        return redirect("/libros/listar")
    