<p>请求查询成交</p>
<p>响应: OnRspQryTrade</p>
<span class="anchor" id="baae9aa6-3de9-4636-b363-1d85f0c906ce"></span>
## 1.函数原型
<p>virtual int ReqQryTrade(CThostFtdcQryTradeField *pQryTrade, int nRequestID) = 0;</p>
<span class="anchor" id="c3b8e775-1039-46c9-a37e-1cab451946c3"></span>
## 2.参数
<p>pQryTrade：查询成交</p>
<pre><code>struct CThostFtdcQryTradeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///成交编号
    TThostFtdcTradeIDType TradeID;
    ///开始时间
    TThostFtdcTimeType TradeTimeStart;
    ///结束时间
    TThostFtdcTimeType TradeTimeEnd;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="b51350d9-74c4-4a70-bf3a-32957cb9eec3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1cb415f1-579c-4b66-b249-0c674623c58d"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="34d7aef6-dae9-4bbf-907b-fab9fefaf054"></span>
## 5.FAQ
<p>无</p>
