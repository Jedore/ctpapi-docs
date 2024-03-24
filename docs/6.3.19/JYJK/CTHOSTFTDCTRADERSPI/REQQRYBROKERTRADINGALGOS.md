<p>请求查询经纪公司交易算法</p>
<p>响应: OnRspQryBrokerTradingAlgos</p>
<span class="anchor" id="e4da2d94-54f0-4e4a-a992-6f77fe99e464"></span>
## 1.函数原型
<p>virtual int ReqQryBrokerTradingAlgos(CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID) = 0;</p>
<span class="anchor" id="680a3923-b3a2-4f82-a80a-6aff123b5e84"></span>
## 2.参数
<p>pQryBrokerTradingAlgos：查询经纪公司交易算法</p>
<pre><code>struct CThostFtdcQryBrokerTradingAlgosField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="4581d9f4-1277-47de-af75-3e9a9af6e4b0"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="389a56f1-e302-468e-af7c-ffb2dc2cbf15"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b75439ef-73d6-4bc8-9473-44055ffbb73f"></span>
## 5.FAQ
<p>无</p>
