<p>请求查询申请组合</p>
<p>响应: OnRspQryCombAction</p>
<span class="anchor" id="ad488f8f-9752-4b59-8e7a-4602ae4e2146"></span>
## 1.函数原型
<p>virtual int ReqQryCombAction(CThostFtdcQryCombActionField *pQryCombAction, int nRequestID) = 0;</p>
<span class="anchor" id="77f86024-02d8-4db6-9a28-ba5c9578fbc7"></span>
## 2.参数
<p>pQryCombAction：申请组合查询</p>
<pre><code>struct CThostFtdcQryCombActionField
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
<span class="anchor" id="f18e6462-abbf-4089-b05d-038f22ee7ff5"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0f871a1b-c051-48a5-97d5-1833691506b2"></span>
## 4.调用示例
<pre><code>CThostFtdcQryCombActionField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
strcpy(a.InstrumentID, "rb1809");//不填写则返回全部
strcpy(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryCombAction(&amp;a, 1);
</code></pre>
<span class="anchor" id="92e541da-b21a-496a-a03a-e955420d8d79"></span>
## 5.FAQ
<p>无</p>
