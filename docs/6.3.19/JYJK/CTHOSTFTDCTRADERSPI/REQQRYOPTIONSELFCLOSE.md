<p>请求查询期权自对冲</p>
<p>响应: OnRspQryOptionSelfClose</p>
<span class="anchor" id="20022319-23fb-487b-b451-8a8689eb3f6f"></span>
## 1.函数原型
<p>virtual int ReqQryOptionSelfClose(CThostFtdcQryOptionSelfCloseField *pQryOptionSelfClose, int nRequestID) = 0;</p>
<span class="anchor" id="40f5c2bb-64b6-4a41-a0c9-41b167bcae30"></span>
## 2.参数
<p>pQryOptionSelfClose：期权自对冲查询</p>
<pre><code>struct CThostFtdcQryOptionSelfCloseField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///期权自对冲编号
    TThostFtdcOrderSysIDType OptionSelfCloseSysID;
    ///开始时间
    TThostFtdcTimeType InsertTimeStart;
    ///结束时间
    TThostFtdcTimeType InsertTimeEnd;
};
</code></pre>
<p>OnRspQryOptionSelfClose：由此能定位一笔期权自对冲的报单</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="115c0378-4f46-4c84-8941-e29049fde543"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="e8396829-3aa4-452b-b53a-c1d73801a2db"></span>
## 4.调用示例
<pre><code>CThostFtdcQryOptionSelfCloseField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryOptionSelfClose(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="6b3570c3-33aa-4145-88d1-353211c8b989"></span>
## 5.FAQ
<p>无</p>
