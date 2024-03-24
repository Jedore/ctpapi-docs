<p>请求查询交易编码</p>
<p>响应: OnRspQryTradingCode</p>
<span class="anchor" id="3249aecd-2ad9-4543-b1a0-9319fc9815ee"></span>
## 1.函数原型
<p>virtual int ReqQryTradingCode(CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID) = 0;</p>
<span class="anchor" id="7dc470ef-6790-447f-b2b7-1efcd01685c9"></span>
## 2.参数
<p>pQryTradingCode：查询交易编码</p>
<pre><code>struct CThostFtdcQryTradingCodeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///客户代码
    TThostFtdcClientIDType ClientID;
    ///交易编码类型
    TThostFtdcClientIDTypeType ClientIDType;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="212ae8a6-5cc3-4114-ab5a-43cc8ed71aca"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b3e75484-809e-4fd5-a342-8d186bb9c2fb"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="306c3da8-1891-4a49-8240-9b3f7792d9ca"></span>
## 5.FAQ
<p>无</p>
