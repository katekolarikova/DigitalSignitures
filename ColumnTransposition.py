def encryptColumnTransposition(text:str, desired_order:str):
    if type(desired_order) != str:
        desired_order = str(desired_order)
    key_len = len(desired_order)
    desired_order = [int(i) for i in desired_order]
    num_of_missing_chars = key_len -( len(text) % key_len)

    # fill free posistions with -
    for i in range(0, num_of_missing_chars):
        text+='-'
    row_length = key_len
    number_of_rows = len(text) // key_len
    columns=[]


    # split text into columns
    for i in range(0, row_length):
        column = []

        # find characters for each column
        for j in range (0, number_of_rows):
            char = text[key_len*j+i]
            column.append(char)
        columns.append(column)

    # reorder columns

    reordered_columns = [columns[k-1] for k in desired_order]
    cipher_text = ""

    # create cipher text from reordered columns
    for column in reordered_columns:
        for char in column:
            cipher_text+=char

    return cipher_text


def decryptColumnTransposition(text,  desired_order):
    if type(desired_order) != str:
        desired_order = str(desired_order)
    row_length = len(desired_order)
    number_of_rows = len(text) // row_length
    columns = []

    # split text into columns
    for i in range(0, row_length):
        column = []

        # find characters for each column
        for j in range(0, number_of_rows):
            char = text[number_of_rows * i + j]
            column.append(char)
        columns.append(column)
    back_to_order = []

    # key for decryption
    # array preparadet
    desired_order = [int(i) for i in desired_order]
    for number in range(1, max(desired_order)+1):
        back_to_order.append(0)

    # fill array with correct order ( look ath cypher key and find the index )
    for number in range(1, max(desired_order)+1):
        index = desired_order.index(number)
        back_to_order[number-1] = index + 1


    reordered_columns = [columns[k-1] for k in back_to_order]
    cipher_text = ""

    # create text - read appropriate string of each column
    for char  in range(0, number_of_rows):
        for column in reordered_columns:
            cipher_text += column[char]
    return cipher_text

# desired_order = createKey("04058")
# secret_message = """RUSKYPREZIDENTVLADIMIRPUTINPRONESLVECTVRTEKTRADICNIPROJEVOSTAVUFEDERACEVENOVALSETOMUZERUSKOMUSIPOKRACOVATVTRANSFORMACIANEMUZESESPOKOJITSESOUCASNYMSTAVEMZMINILSTOUPAJICIPOCETCHUDYCHIZAOSTALOUINFRASTRUKTURUNUTNOUPODPORUDUCHODCUMIMLADYMRODINYMABYSEZVRYTILNEPRIZNIVYDEMOGRAFICKYVYVOJ"""
# test_messgae = "THESIMPLESTPOSSIBLETRANSPOSITIONSXX"
# test = encryptColumnTransposition(test_messgae, desired_order)
# decryptColumnTransposition(test, desired_order )

