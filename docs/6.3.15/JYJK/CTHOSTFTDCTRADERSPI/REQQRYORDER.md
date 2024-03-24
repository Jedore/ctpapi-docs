<p>请求查询报单</p>
<p>响应: OnRspQryOrder</p>
<span class="anchor" id="4bbce22c-67bf-4585-84ee-83ff73598e37"></span>
## 1.函数原型
<p>virtual int ReqQryOrder(CThostFtdcQryOrderField *pQryOrder, int nRequestID) = 0;</p>
<span class="anchor" id="9d2b2b96-8b6c-4310-bbd8-52edb12bb980"></span>
## 2.参数
<p>pQryOrder：查询报单</p>
<pre><code>struct CThostFtdcQryOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///报单编号
    TThostFtdcOrderSysIDType OrderSysID;
    ///开始时间
    TThostFtdcTimeType InsertTimeStart;
    ///结束时间
    TThostFtdcTimeType InsertTimeEnd;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="472df68b-21a7-4593-a452-71764147d7ce"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="71b00737-c5cb-4f9f-ab7f-84135972660a"></span>
## 4.调用示例
<pre><code>CThostFtdcQryOrderField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryOrder(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="bf9b87f7-d704-4e21-85b0-8a180a6fb879"></span>
## 5.FAQ
<p>无</p>
