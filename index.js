
const options = {};

options.ip = '127.0.0.1';
options.port = parseInt(process.env.PORT);
options.unixsocket = require('path').join(require('os').tmpdir(), 'app_name');
options.config = { name: 'Total.js' };
options.sleep = 3000;
options.inspector = 9229;
options.watch = ['private'];
ptions.livereload = 'https://yourhostname';

Enables cluster:
options.cluster = 'auto';
options.cluster_limit = 10; // max 10. threads (works only with "auto" scaling)

Enables threads:
options.cluster = 'auto';
options.cluster_limit = 10; // max 10. threads (works only with "auto" scaling)
options.timeout = 5000;
options.threads = '/api/';
ptions.logs = 'isolated';

var type = process.argv.indexOf('--release', 1) !== -1 || process.argv.indexOf('release', 1) !== -1 ? 'release' : 'debug';
require('total4/' + type)(options);
require('total4').http('release', options);