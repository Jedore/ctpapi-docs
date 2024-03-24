<p>请求查询经纪公司交易算法</p>
<p>响应: OnRspQryBrokerTradingAlgos</p>
<span class="anchor" id="4b6e1ef5-9d74-4047-8607-8fd8e9b377fc"></span>
## 1.函数原型
<p>virtual int ReqQryBrokerTradingAlgos(CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID) = 0;</p>
<span class="anchor" id="9949f054-89b0-4bd5-9a42-d298aabbf6e4"></span>
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
<span class="anchor" id="18980f21-9eb1-4b7a-bcbb-74a4fbe337ad"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="9c79a036-0b38-41ce-bf87-602f2c944a43"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="c78bc0d4-664b-4aaf-8765-97b3eaf8413e"></span>
## 5.FAQ
<p>无</p>
