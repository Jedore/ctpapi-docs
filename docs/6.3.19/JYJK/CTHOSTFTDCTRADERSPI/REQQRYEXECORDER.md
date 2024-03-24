<p>请求查询执行宣告</p>
<p>响应: OnRspQryExecOrder</p>
<span class="anchor" id="dc922e67-3606-4b9f-85f7-7d2d8e3a22ad"></span>
## 1.函数原型
<p>virtual int ReqQryExecOrder(CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID) = 0;</p>
<span class="anchor" id="a4a7ef9e-f91d-482a-a2bf-63c01848e3da"></span>
## 2.参数
<p>pQryExecOrder：执行宣告查询</p>
<pre><code>struct CThostFtdcQryExecOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///执行宣告编号
    TThostFtdcExecOrderSysIDType ExecOrderSysID;
    ///开始时间
    TThostFtdcTimeType InsertTimeStart;
    ///结束时间
    TThostFtdcTimeType InsertTimeEnd;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="85de3665-1675-4b00-a1d7-a4c7f9c7131c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3fe2152d-f436-49d5-9110-a279710866d8"></span>
## 4.调用示例
<pre><code>CThostFtdcQryExecOrderField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryExecOrder(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="36a50690-20d6-470a-a72b-56c7f8f9eb88"></span>
## 5.FAQ
<p>无</p>
