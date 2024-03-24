<p>目前，各交易所提供的行情存在一定的差异，主要体现在字段数量、字段计算方法、字段含义上，甚至行情每秒tick数都不尽相同。CTP对交易所的行情只做转发，但对于有些交易所不发的字段，会做一定程度的补充，例如郑商所的成交金额，交易所不发这个字段，但该字段对于行情又十分重要，因此CTP会计算并补填；对于交易所有值的字段，CTP不会对其做更改，只做转发。</p>
<p>本文针对CTP给出的各所行情，选取一些重要差异，逐一说明，以帮助用户更快上手，降低开发成本。交易所行情本身的差异不在本文讨论范围。如需了解行情的订阅方法，请参阅<a href="../../HQJK/_HQJK/">行情接口</a>。</p>
<span class="anchor" id="1a4085dd-fb21-4d7b-bc72-d180102753b3"></span>
## 1.字段差异
<ul>
<li>ExchangeID（交易所ID）</li>
</ul>
<p>期货普通前置不推送exchangeid； 期货mdfront推送exchangeid ；个股的普通前置推送exchangeid</p>
<ul>
<li>Tradingday（交易日）</li>
</ul>
<p>郑商所行情的Tradingday是自然日，其他交易所的Tradingday都是交易日。</p>
<ul>
<li>TrunOver（成交金额）</li>
</ul>
<p>郑商所行情中，不推送成交金额，CTP的TCP行情会自行计算并填补，成交金额=成交均价*成交数量。</p>
<ul>
<li>AveragePrice（成交均价）</li>
</ul>
<p>除了郑商所外，其他交易所都不推送成交均价，CTP的TCP行情会自行计算并填补，成交均价=成交金额/成交数量</p>
<span class="anchor" id="df6309f9-27a6-4949-a4bd-665e746e5a9d"></span>
## 2.每秒tick数
<p>郑商所的行情可以配置为4Tick/秒或2Tick/秒，该配置在CTP的郑商所报盘ini里。</p>
<blockquote>
<p>czcemdserver.ini中，MarketID=ZCE001为两笔，行情源是tcp行情。MarketID=ZCE011为四笔，行情源是udp行情。如欲配置成4笔，<strong>请咨询上期技术当前mdserver版本是否支持</strong>。</p>
<p>使用mdfront的，在mdfront.ini中，郑商所配置下，ProtocolVersion=2为两笔，ProtocolVersion=11为四笔。</p>
<p>特别注意：交易所4Tick/秒的行情不会推送日终收盘价，CTP转发出来的收盘价是夜盘的收盘价，而非日终收盘价，请注意区分。</p>
</blockquote>
<p>其他交易所的行情只能是2Tick/秒，即500毫秒推一次，一秒两次。</p>
<span class="anchor" id="b95f377c-2b19-4e4d-b548-c70a57fb65de"></span>
## 3.组合合约行情
<p>只有大商所和郑商所有组合合约行情，其他交易所没有组合合约行情。</p>
<p>组合行情仅有少数字段有值，例如买卖价量、涨跌停板；大部分字段都没有值，例如最新价、成交金额、成交量等。</p>
<blockquote>
<p><strong>特别提醒</strong>：部分终端的组合行情有最新价，是因为终端自己计算了最新价。并非行情订阅的有问题。</p>
</blockquote>
<span class="anchor" id="fc095551-c6bf-4804-b3dd-f633d4995274"></span>
## 4.UDP行情和TCP行情区别
<p>UDP行情只做纯转发，因此交易所不发的字段，在UDP行情里就保持为空转发出去。</p>
<p>TCP行情会补填一些字段。比如郑商所的Tradingday字段和AveragePrice字段，交易所行情没有这个字段，因此是空的，但是TCP行情会去补填。</p>
<p>UDP行情和TCP行情的订阅方法，请参阅<a href="../../HQJK/CTHOSTFTDCMDAPI/CREATEFTDCMDAPI/">CreateFtdcMdApi</a></p>
