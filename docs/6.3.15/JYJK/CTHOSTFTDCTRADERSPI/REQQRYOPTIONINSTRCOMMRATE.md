<p>请求查询期权合约手续费</p>
<p>响应: OnRspQryOptionInstrCommRate</p>
<span class="anchor" id="558eb01f-47b3-4afd-bf99-73b64c833e30"></span>
## 1.函数原型
<p>virtual int ReqQryOptionInstrCommRate(CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID) = 0;</p>
<span class="anchor" id="91681c72-d996-436c-adff-c99b73f7b62f"></span>
## 2.参数
<p>pQryOptionInstrCommRate：期权手续费率查询</p>
<pre><code>struct CThostFtdcQryOptionInstrCommRateField
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
<span class="anchor" id="3c74d093-3999-45fb-ba70-ea7449c9c6be"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="07058904-7427-49f6-967a-9242f4a514a4"></span>
## 4.调用示例
<pre><code>CThostFtdcQryOptionInstrCommRateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqQryOptionInstrCommRate(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="aec2838c-8398-4cd4-8c48-2ae2692e0be6"></span>
## 5.FAQ
<p>无</p>
