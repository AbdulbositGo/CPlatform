from django.template.loader import get_template

def get_cloudinary_image(
    instance,
    field_name="image",
    as_html=False,
    width=200
    ):
    if not hasattr(instance, field_name):
        return ''
    image_object = getattr(instance, field_name)
    if not image_object:
        return ''
    image_options = {
        'width': width
    }
    if as_html:
        return image_object.image(**image_options)
    return image_object.build_url(**image_options)

def get_cloudinary_video(
        instance,
        field_name="video",
        as_html=False,
        width=None,
        heigth=None,
        sign_url=False,
        fetch_format='auto',
        quality='auto',
        control=True,
        autoplay=True,
        template_name="video.html"
    ):
    if not hasattr(instance, field_name):
        return ''
    video_object = getattr(instance, field_name)
    if not video_object:
        return ''
    video_options = {
        'sign_url': sign_url,
        'fetch_format': fetch_format,
        'quality': quality,
        'controls': control,
        'autoplay': autoplay,
    }
    
    if width:
        video_options['width'] = width
    if heigth:
        video_options['heigth'] = heigth
    if width and heigth:
        video_options['crop'] = 'limit'
        
    url = video_object.build_url(**video_options)
    
    if as_html:
        return get_template(template_name).render({
            'url': url,
            'thumbnail': get_cloudinary_image(instance, field_name='thumbnail', width=width)
        })
    
    return 