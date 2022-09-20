from utils import *

tab1, tab2 = st.tabs(['Test Görseli Üzerinde Çalışacağım', 'Kendi Görselimle Çalışacağım'])

with tab1:
    st.title('Renk Paleti Oluşturma')
    st.subheader('Test görseli')
    st.image('test.jpeg', use_column_width=True)
    tolerans = st.text_input('Tolerans', '10')
    st.caption('Tolerans, paletteki renklerin farklı olmasını sağlar. '
            ' Baskın renklerin olduğu görsellerde tolerans değerini yükseltmeniz önerilir.')
    zoom = st.text_input('Yakınlaştırma', '2.5')
    st.caption('Çıktı görselin yakınlaştırılma oranıdır. Değer büyüdükçe, çıktı görseli daha da yakınlaştırılır.')
    if st.button('Renk Paleti Oluştur'):
        exact_color('test.jpeg', 900, int(tolerans), float(zoom))
        st.image('output.png', use_column_width=True)
        st.caption(
            "Renk Paleti için kaynak kodu: https://towardsdatascience.com/image-color-extraction-with-python-in-4-steps-8d9370d9216e")

with tab2:
    st.title('Renk Paleti Oluşturma')
    uploaded = st.file_uploader('Görsel yükleyin', type=['png', 'jpg', 'jpeg'])
    img = None

    if uploaded:
        st.subheader('Görsel yükleniyor...')
        st.image(uploaded, use_column_width=True)
        img = Image.open(uploaded, mode='r')
        img.save('uploaded.png')
    tolerans = st.text_input('Tolerans', '10', key='tolerans_self')
    st.caption('Tolerans, paletteki renklerin farklı olmasını sağlar. '
               ' Baskın renklerin olduğu görsellerde tolerans değerini yükseltmeniz önerilir.')
    zoom = st.text_input('Yakınlaştırma', '2.5', key='zoom_self')
    st.caption('Çıktı görselin yakınlaştırılma oranıdır. Değer büyüdükçe, çıktı görseli daha da yakınlaştırılır.')
    if st.button('Renk Paleti Oluştur', key='button_self'):
        exact_color('uploaded.png', 900, int(tolerans), float(zoom))
        st.image('output.png', use_column_width=True)
        st.caption("Renk Paleti için kaynak kodu: https://towardsdatascience.com/image-color-extraction-with-python-in-4-steps-8d9370d9216e")

