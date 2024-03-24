<p>请求查询交易编码</p>
<p>响应: OnRspQryTradingCode</p>
<span class="anchor" id="09b6fddb-58a9-482b-98b4-c975315f58bf"></span>
## 1.函数原型
<p>virtual int ReqQryTradingCode(CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID) = 0;</p>
<span class="anchor" id="ac2a3233-73a6-49ce-8c6b-542e453330f7"></span>
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
<span class="anchor" id="d950b1b2-1a48-4184-abe6-64ed3bef3bb5"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a3eff2c2-a997-4899-9c3c-607ca3c73ffb"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4af162e6-4849-42ac-98b2-2f4821400bae"></span>
## 5.FAQ
<p>无</p>
