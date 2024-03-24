<p>请求查询执行宣告</p>
<p>响应: OnRspQryExecOrder</p>
<span class="anchor" id="c93dcfea-6c39-42f1-be25-ce8a53d63c80"></span>
## 1.函数原型
<p>virtual int ReqQryExecOrder(CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID) = 0;</p>
<span class="anchor" id="b606fd5d-61c0-45b0-99fd-7e3da6228391"></span>
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
<span class="anchor" id="6d5ada99-01d5-485b-9594-d0198862306f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7c26afd6-ae99-41e1-a855-d5bcbdfca48f"></span>
## 4.调用示例
<pre><code>CThostFtdcQryExecOrderField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryExecOrder(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="c35b6fa0-280a-4c7c-a76c-fddb6c7098b6"></span>
## 5.FAQ
<p>无</p>
