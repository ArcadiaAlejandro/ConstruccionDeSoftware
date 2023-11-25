import {PythonShell} from 'python-shell';

PythonShell.run(
    'Conection.py', //aqui va el nombre del archivo python
    null,
    function (err){
        if(err) throw err;
        console.log('finished');
    }
);