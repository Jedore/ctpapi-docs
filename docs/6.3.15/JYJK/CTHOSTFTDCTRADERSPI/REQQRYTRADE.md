<p>请求查询成交</p>
<p>响应: OnRspQryTrade</p>
<span class="anchor" id="880b608e-e12d-4736-873f-6ffaf924f41a"></span>
## 1.函数原型
<p>virtual int ReqQryTrade(CThostFtdcQryTradeField *pQryTrade, int nRequestID) = 0;</p>
<span class="anchor" id="b59652da-8c89-45c3-b484-753d5b6945f7"></span>
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
<span class="anchor" id="9fef50ee-bf45-4ae6-946b-5882492229d2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="55fb04bd-90e0-4220-82b5-48e337b24ca9"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4a741cf8-66cd-4a0c-a2f9-8e910ccf96e1"></span>
## 5.FAQ
<p>无</p>
