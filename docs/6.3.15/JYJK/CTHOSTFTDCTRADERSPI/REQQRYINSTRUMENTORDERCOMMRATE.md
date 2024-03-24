<span class="anchor" id="283c557e-7ae5-4fc9-adbb-54921437444b"></span>
## 1.说明
<p>请求查询报单手续费</p>
<p>响应: OnRspQryInstrumentOrderCommRate</p>
<span class="anchor" id="4b475b96-9718-4ce7-93d6-8fd1b9fa71c2"></span>
## 2.函数原型
<p>virtual int ReqQryInstrumentOrderCommRate(CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID) = 0;</p>
<span class="anchor" id="4701197f-fd46-473a-ab0c-9bcfbaf172bc"></span>
## 3.参数
<p>pQryInstrumentOrderCommRate：报单手续费率查询</p>
<pre><code>struct CThostFtdcQryInstrumentOrderCommRateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="a4a51c56-c8e3-4477-9af4-90b6c465b7c9"></span>
## 4.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="fc29360e-00f0-4e53-a5dc-b912772a5eb7"></span>
## 5.调用示例
<pre><code>CThostFtdcQryInstrumentOrderCommRateField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
strcpy(a.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqQryInstrumentOrderCommRate(&amp;a, 1);
</code></pre>
<span class="anchor" id="e7ce6dd9-c8f0-420b-a328-70c934d94c2d"></span>
## 6.FAQ
<p>无</p>
