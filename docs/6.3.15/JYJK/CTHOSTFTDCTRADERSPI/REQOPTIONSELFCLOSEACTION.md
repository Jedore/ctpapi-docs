<p>期权自对冲操作请求</p>
<p>错误响应: OnErrRtnOptionSelfCloseAction，OnRspOptionSelfCloseAction</p>
<p>正确响应: OnRtnOptionSelfClose</p>
<span class="anchor" id="d47dfb8a-d948-464e-8347-73de491a7860"></span>
## 1.函数原型
<p>virtual int ReqOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, int nRequestID) = 0;</p>
<span class="anchor" id="3f882a01-2961-422a-8b9e-b7d4ea4aad06"></span>
## 2.参数
<p>pInputOptionSelfCloseAction：输入期权自对冲操作</p>
<pre><code>struct CThostFtdcInputOptionSelfCloseActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///期权自对冲操作引用
    TThostFtdcOrderActionRefType OptionSelfCloseActionRef;
    ///期权自对冲引用
    TThostFtdcOrderRefType OptionSelfCloseRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///期权自对冲操作编号
    TThostFtdcOrderSysIDType OptionSelfCloseSysID;
    ///操作标志
    TThostFtdcActionFlagType ActionFlag;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///期权行权的头寸是否自对冲
    TThostFtdcOptSelfCloseFlagType OptSelfCloseFlag;
};
</code></pre>
<p>OptionSelfCloseRef：对应要撤销的期权自对冲的引用</p>
<p>FrontID：对应要撤销的期权自对冲的前置编号</p>
<p>SessionID：对应要撤销的期权自对冲的会话编号</p>
<p>ExchangeID：对应要撤销的期权自对冲的交易所编号</p>
<p>ActionFlag：支持删除，不支持修改</p>
<p>InstrumentID：对应要撤销的期权自对冲的合约代码</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="e1514a03-564a-40c4-8909-fd6822e7419a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7399984f-0537-4c5b-ab8c-03b1ae91489b"></span>
## 4.调用示例
<pre><code>CThostFtdcInputOptionSelfCloseActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001"); 
strcpy_s(a.OptionSelfCloseRef, "000000258");//期权自对冲引用
a.FrontID = 1;
a.SessionID = 6442531;
strcpy_s(a.ExchangeID, "SHFE");
a.ActionFlag = THOST_FTDC_AF_Delete;
strcpy_s(a.UserID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqOptionSelfCloseAction(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="1c155fdf-b8b0-4eff-bd91-57519ccb1b01"></span>
## 5.FAQ
<p>无</p>
