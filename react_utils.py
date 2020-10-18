import qrcode
import os
import json
#Generating react validation states
def generateReactValidator(data,conn,page):
    states = []
    validators = []

    labels={}
    hints = {}
    
    form=""
    
    generalValidator = " const onLoginClick = () => {\nif"
    
    for option in data:

        d = option.get("name")
      
        f = d.split()[0]
        f2 = " ".join(d.split()[1:]).title().replace(" ", "")
        newd=conn+f.title()+f2
        
        dft = "\"\""
        if option.get("type") == "date":
          dft = "new Date()"
        elif option.get("type") == "auto":
          dft = "{ }"
          
        state = "const [" + newd + ", set" + d.title().replace(" ", "") + "] = useState({ value: "+dft+", error: \"\" })"
        
        if option.get("type") == "date":
          validator= "const on" + d.title().replace(" ","") + "Change = (date) => {"+\
                       "set" + d.title().replace(" ","") + "({ value: date, error: \"\"});"+\
                      " }"
        elif option.get("type") == "auto":
          validator="const on" + d.title().replace(" ","") + "Change = (event,v) => {"+\
          "if (v.id ==null) {"+\
          "set" + d.title().replace(" ","") + "({ value: {}, error:  <Translate>"+\
              "{({ translate }) => translate('"+page+".forms."+"hints."+conn+"_"+d.lower().replace(" ","_")+ "')}"+\
            "</Translate> })"+\
          "} else {"+\
          "set" + d.title().replace(" ","") + "({ value:v, error: \"\"});"+\
          "}};"

        else:
          validator="const on" + d.title().replace(" ","") + "Change = (event) => {"+\
          "if (event.target.value === \"\") {"+\
          "set" + d.title().replace(" ","") + "({ value: '', error:  <Translate>"+\
              "{({ translate }) => translate('"+page+".forms."+"hints."+conn+"_"+d.lower().replace(" ","_")+ "')}"+\
            "</Translate> })"+\
          "} else {"+\
          "set" + d.title().replace(" ","") + "({ value: event.target.value, error: \"\"});"+\
          "}};"

        if option.get("type")=='auto':
          generalValidator=generalValidator+"(" + newd + ".value.id == null) {\n"+\
          "set" + d.title().replace(" ","") + "({ value: {}, error:  <Translate>"+\
              "{({ translate }) => translate('"+page+".forms."+"hints."+conn+"_"+d.lower().replace(" ","_")+ "')}"+\
            "</Translate> })\n}else if"
        else:
          generalValidator=generalValidator+"(" + newd + ".value === \"\") {\n"+\
          "set" + d.title().replace(" ","") + "({ value: \"\", error:  <Translate>"+\
              "{({ translate }) => translate('"+page+".forms."+"hints."+conn+"_"+d.lower().replace(" ","_")+ "')}"+\
            "</Translate> })\n}else if"
         
        if option.get("type")=="select" or option.get("type")=="date" or option.get("type")=="auto":
          hints[conn + "_" + d.lower().replace(" ", "_")] = "Select " + conn + " " + d.lower() + ""
        else:
          hints[conn + "_" + d.lower().replace(" ", "_")] = "Enter " + conn + " " + d.lower() + ""
        
        labels[conn+"_"+d.lower().replace(" ","_")]= conn.capitalize() + " " + d.lower()
        if option.get("type")=="text":
          form=form+"\n <Box mt={2}>\n"+\
                          "<Translate>\n"+\
                             "{({ translate }) => (\n"+\
                               "<TextField\n"+\
                                 "size='small'\n"+\
                                 "variant='outlined'\n"+\
                                 "color='primary'\n" + \
                                  "type='"+option.get("type")+"'\n" + \
                                 "value={"+newd+ ".value}\n"+\
                                 "placeholder={translate(\n"+\
                                  "'"+page+".forms."+"hints."+conn+"_"+d.lower().replace(" ","_")+ "'\n"+\
                                 ")}\n"+\
                                 "label={\n"+\
                                  " <Translate id='"+page+".forms."+"labels."+conn+"_"+d.lower().replace(" ","_")+"' />\n"+\
                                 "}\n"+\
                                " fullWidth\n"+\
                                " onChange={on" + d.title().replace(" ","") + "Change}\n"+\
                                " helperText={"+newd+".error}\n"+\
                                " error={"+newd+".error !== \"\"}\n"+\
                               "/>\n"+\
                             ")}\n"+\
                           "</Translate>\n"+\
                         "</Box>"
        elif option.get("type")=="select":

          form=form+ "\n <Box mt={2}>\n"+\
          "<FormControl\n"+\
            "fullWidth\n"+\
            "variant=\"outlined\"\n"+\
            "size=\"small\"\n"+\
            "error={"+newd+".error !== \"\"}>\n"+\
            " <InputLabel>\n"+\
              " <Translate id='"+page+".forms."+"labels."+conn+"_"+d.lower().replace(" ","_")+"' />\n"+\
            "</InputLabel>\n"+\
            "<Select\n"+\
              "label={<Translate id='"+page+".forms."+"labels."+conn+"_"+d.lower().replace(" ","_")+"' />}\n"+\
               "value={"+newd+ ".value}\n"+\
             " onChange={on" + d.title().replace(" ","") + "Change}>\n"+\
             "{orgs.map((org, i) => (\n"+\
               "<MenuItem value={"+"org.id"+"}>{"+"org.name"+"}</MenuItem>\n"+\
              " ))}\n"+\
            " </Select>\n"+\
            "<FormHelperText>{"+newd+".error}</FormHelperText>\n"+\
         " </FormControl>\n"+\
       "  </Box>"

        elif option.get("type") == "date":
          form=form+"\n  <Box mt={2}>\n"+\
                         " <DatePicker\n"+\
                            " fullWidth\n"+\
                            "disableToolbar\n"+\
                            " variant=\"inline\"\n"+\
                            " format=\"yyyy-MM-dd\"\n"+\
                            " margin=\"dense\"\n"+\
                           " disablePast\n"+\
                           " autoOk\n"+\
                           " label={\n"+\
                             " <Translate id='"+page+".forms."+"labels."+conn+"_"+d.lower().replace(" ","_")+"' />\n"+\
                           " }\n"+\
                            "value={"+newd+ ".value}\n"+\
                            "inputVariant='outlined'\n"+\
                          " onChange={on" + d.title().replace(" ","") + "Change}\n"+\
                            " InputProps={{\n"+\
                             " disableUnderline: true,\n"+\
                             " style: { paddingRight: 0 },\n"+\
                           " }}\n"+\
                         " /> \n"+\
                       " </Box> "

        elif option.get("type") == 'auto':
          form=form+"\n<Box mt={2}>\n"+\
             " <Autocomplete\n"+\
               " fullWidth\n"+\
               " openOnFocus \n"+\
               " options={"+"options"+"}\n"+\
               " getOptionLabel={(option) => option.name}\n" + \
                 " onChange={on" + d.title().replace(" ","") + "Change}\n"+\
               " renderInput={(params) => (\n"+\
                 " <TextField \n"+\
                   " {...params} \n"+\
                   " fullWidth \n"+\
                     " label={\n"+\
                             " <Translate id='"+page+".forms."+"labels."+conn+"_"+d.lower().replace(" ","_")+"' />\n"+\
                           " }\n"+\
                    " variant=\"outlined\"\n"+\
                   " size=\"small\"\n" + \
                      " helperText={"+newd+".error}\n"+\
                   " error={"+newd+".error !== \"\"}\n"+\
                 " />\n"+\
                ")}\n"+\
              " />\n"+\
           "</Box>"

        else:
          form=form+"\n <Box mt={2}>\n"+\
                          "<Translate>\n"+\
                             "{({ translate }) => (\n"+\
                               "<TextField\n"+\
                                 "size='small'\n"+\
                                 "variant='outlined'\n"+\
                                 "color='primary'\n" + \
                                  "type='"+option.get("type")+"'\n" + \
                                 "value={"+newd+ ".value}\n"+\
                                 "placeholder={translate(\n"+\
                                  "'"+page+".forms."+"hints."+conn+"_"+d.lower().replace(" ","_")+ "'\n"+\
                                 ")}\n"+\
                                 "label={\n"+\
                                  " <Translate id='"+page+".forms."+"labels."+conn+"_"+d.lower().replace(" ","_")+"' />\n"+\
                                 "}\n"+\
                                " fullWidth\n"+\
                                " onChange={on" + d.title().replace(" ","") + "Change}\n"+\
                                " helperText={"+newd+".error}\n"+\
                                " error={"+newd+".error !== \"\"}\n"+\
                               "/>\n"+\
                             ")}\n"+\
                           "</Translate>\n"+\
                         "</Box>"

        states.append(state)
        validators.append(validator)

    trans = {
        "labels": labels,
        "hints": hints,
    }

    generalValidator=generalValidator+"{}}"
    return generalValidator,states, validators,json.dumps(trans),form
    
#Generating qr codes from list
# def generateQrcode(data):

#     q = qrcode.QRCode(border=2)
#     q.add_data("CENT 20200610 1 0019")
#     q.make(fit=True)

#     img = q.make_image(fill_color="black")
    
    # os.makedirs(os.getcwd()+"/generated/codes")
    # print(os.getcwd())
    # img.save('generated/codes/Gilbert Tuyishime.png')

options = [
  {"name": "description", "type": "text"},
  ]

g, states, validators,trans,form = generateReactValidator(options,"reverse","transaction")

print("_______________________Translations_____________________")
print(trans)

print("_______________________States_____________________")
for s in states:
    print(s)

print("_______________________Validators_____________________")
for v in validators:
    print(v)

print("_______________________General validators_____________________")
print(g)


print("_______________________Form_____________________")
print(form)
