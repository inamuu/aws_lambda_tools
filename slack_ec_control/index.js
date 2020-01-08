'use strict';

const AWS = require('aws-sdk');
var targetId = '';
var displayMsg = '';

// EC2 インスタンスのステータスを確認する
function statusEC2Instance(region, instanceId) {
    const ec2 = new AWS.EC2({ region: region });
    const params = {
        InstanceIds: [instanceId],
        DryRun: false
    };
    return new Promise((resolve, reject) => {
        ec2.describeInstances(params, (err, data) => {
            if (err) reject(err);
            else    resolve(data.Reservations[0].Instances[0].State.Name);
        }); 
    });
}

// EC2 インスタンスを起動する
function startEC2Instance(region, instanceId) {
    const ec2 = new AWS.EC2({ region: region });
    const params = {
        InstanceIds: [instanceId],
        DryRun: false,
    };
    return new Promise((resolve, reject) => {
        ec2.startInstances(params, (err, data) => {
            if (err) reject(err);
            else     resolve(data.StartingInstances[0].CurrentState.Name);
        }); 
    });
}


// EC2 インスタンスを停止する
function stopEC2Instance(region, instanceId) {
    const ec2 = new AWS.EC2({ region: region });
    const params = {
        InstanceIds: [instanceId],
        DryRun: false,
    };
    return new Promise((resolve, reject) => {
        ec2.stopInstances(params, (err, data) => {
            if (err) reject(err);
            else     resolve(data.StoppingInstances[0].CurrentState.Name);
        }); 
    });
}

// 関数指定してインスタンスを制御します。
function executeControl(ec2Function) {
    //const result = { EC2: null };
    var result = '';
    const a = ec2Function(process.env.EC2_REGION, targetId)
        .then(data => {
            //result = { result: 'OK', data: data };
            result = data;
        }).catch(err => {
            result = { result: 'hoge', data: err };
        });
    return Promise.all([a]).then(() => result );
}

function getSuccessfulResponse(message, result) {
    switch (result) {
        case 'running':
            var displayMsg = '起動しています';
            break;
        case 'stopped':
            var displayMsg = '停止しています';
            break;
        case 'pending':
            var displayMsg = '起動中です';
            break;
        default:
            var displayMsg = 'ec2コマンドで制御できるインスタンスではありません';
    }
    
    
    return {
        //"response_type": "in_channel",
        "attachments": [
            {
                "color": "#87ceeb",
                "text": '*実行コマンド*' + '\n' + 
                message + '\n' +
                '*実行結果*' + '\n' +
                displayMsg
            },
        ],
    };
}

function getErrorResponse(message) {
    return {
        "response_type": "ephemeral",
        "attachments": [
            {
                "color": "#ff0000",
                "title": 'Error',
                "text": message,
            },
        ],
    };
}

exports.handler = (event, context, callback) => {
    console.log(event)
    if (!event.token || event.token !== process.env.SLASH_COMMAND_TOKEN)
        callback(null, getErrorResponse('Invalid token'));
    if (!event.text)
        callback(null, getErrorResponse('Parameter missing'));

    var target = event.text.split(' ')[0];
    switch (target) {
        case 'app1':
            targetId = 'i-XXXXX';
            break;
        case 'app2':
            targetId = 'i-XXXXX';
            break;
        case 'app33':
            targetId = 'i-XXXXX';
            break;
    }
    
    if (event.text.match(/start/)) {
        executeControl(startEC2Instance).then(result => { callback(null, getSuccessfulResponse(target + ' Starting...', result)); });
    } else if (event.text.match(/stop/)) {
        executeControl(stopEC2Instance).then(result => { callback(null, getSuccessfulResponse(target + ' Stopping...', result)); });
    } else if (event.text.match(/status/)) {
        executeControl(statusEC2Instance).then(result => { callback(null, getSuccessfulResponse(target + ' Get status...', result)); });
    } else {
        callback(null, getErrorResponse('Unknown parameters'));
    }
};

