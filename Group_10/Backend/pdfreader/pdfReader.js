var path = require('path')
var filePath = path.join(__dirname, 'Quiz2.pdf')
var extract = require('pdf-text-extract')
extract(filePath, function (err, pages) {
    if (err) {
        console.dir(err)
        return
    }
    console.log(pages)
    str = pages[0]
    str=str.replace(/\r/g,'')
    console.log([str])
    var i = 0;
    while(i < str.length)
    {
        //Get quizName from PDF
        var quizname='';
        while(str[i] != '\n')
        {
            quizname += str[i++]
        }
        // console.log(quizname, i);
        i++;

        //Get accessKey from PDF
        var accesskey='';
        while(str[i] != '\n')
        {
            accesskey += str[i++]
        }
        // console.log(accesskey, i);
        i++;

        //Get startTime from PDF
        var starttime='';
        while(str[i] != '\n')
        {
            starttime += str[i++]
        }
        // console.log(starttime, i);
        i++;

        //Get endTime from PDF
        var endtime='';
        while(str[i] != '\n')
        {
            endtime += str[i++]
        }
        // console.log(endtime, i);
        i++;
        i++;

        //Get qData from PDF
        var qdata=[];
        while(str[i] != '\n' && str[i] != '!')
        {

            //Get questionName from PDF
            var questionText =''
            while(str[i] != '\n')
            {
                questionText += str[i++]
            }
            i++;

            //Get options from PDF
            var options=[]
            while(str[i] != '\n')
            {
                var option = '';
                while(str[i] != '\n')
                {
                    option += str[i++]
                }
                i++
                options.push(option);
            }
            i++
            qdata.push({
                questiontext : questionText,
                options : options
            });
        }

        // console.log(qdata, str[i]);

        while(str[i] != '\n')
        {
            i++;
        }
        i++
        // console.log(i,str[i]);
        var answers = [];
        while(str[i] != '\n' && i < str.length)
        {
            var answer = '';

            while(str[i] != '\n')
            {
                answer += str[i++];
            }

            i++;
            // console.log(answer,i,str[i]);
            answers.push(answer-1);

        }

        console.log(quizname);
        console.log(accesskey);
        console.log(starttime);
        console.log(endtime);
        console.log(qdata);
        console.log(answers);


        break;
    }

})
