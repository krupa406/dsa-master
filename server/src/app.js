const express = require('express');
const cors = require('cors');
const technologiesRouter = require('./routes/technologies');
const levelsRouter = require('./routes/levels');
const modulesRouter = require('./routes/modules');
const labsRouter = require('./routes/labs');
const quizzesRouter = require('./routes/quizzes');
const errorHandler = require('./middleware/errorHandler');
const requestLogger = require('./middleware/requestLogger');

const app = express();
app.use(cors({ origin: 'http://localhost:5173' }));
app.use(express.json());
app.use(requestLogger);

app.get('/api/health', (req, res) => res.json({ status: 'ok', timestamp: new Date().toISOString() }));
app.use('/api/technologies', technologiesRouter);
app.use('/api/technologies', levelsRouter);
app.use('/api/technologies', modulesRouter);
app.use('/api/technologies', labsRouter);
app.use('/api/technologies', quizzesRouter);
app.use(errorHandler);
module.exports = app;
