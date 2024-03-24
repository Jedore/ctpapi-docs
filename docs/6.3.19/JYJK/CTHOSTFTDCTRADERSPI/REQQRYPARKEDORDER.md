<p>请求查询预埋单</p>
<p>响应: OnRspQryParkedOrder</p>
<span class="anchor" id="baf48873-4363-4460-8352-69c78aab9dba"></span>
## 1.函数原型
<p>virtual int ReqQryParkedOrder(CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID) = 0;</p>
<span class="anchor" id="be8bc1fa-c9b6-406b-a524-f8f2ec21ed48"></span>
## 2.参数
<p>pQryParkedOrder：查询预埋单</p>
<pre><code>struct CThostFtdcQryParkedOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="25f6de44-0330-4f6a-b0db-656bbba14127"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="fca373ab-1371-4fcf-9768-7e91056223f3"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="72b5b2e7-71c7-4f0c-99db-eae30b72c05a"></span>
## 5.FAQ
<p>无</p>
