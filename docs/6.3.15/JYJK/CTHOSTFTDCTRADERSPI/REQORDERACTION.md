<p>报单操作请求</p>
<p>错误响应: OnRspOrderAction，OnErrRtnOrderAction</p>
<p>正确响应：OnRtnOrder</p>
<span class="anchor" id="9a30162f-7479-4f72-acc2-6919d81dc6ec"></span>
## 1.函数原型
<p>virtual int ReqOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="537b7c2a-f86c-437e-8e0c-5cbcb841147b"></span>
## 2.参数
<p>pInputOrderAction：输入报单操作</p>
<pre><code>struct CThostFtdcInputOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///报单操作引用
    TThostFtdcOrderActionRefType OrderActionRef;
    ///报单引用
    TThostFtdcOrderRefType OrderRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///报单编号
    TThostFtdcOrderSysIDType OrderSysID;
    ///操作标志
    TThostFtdcActionFlagType ActionFlag;
    ///价格
    TThostFtdcPriceType LimitPrice;
    ///数量变化
    TThostFtdcVolumeType VolumeChange;
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
};
</code></pre>
<p>OrderRef：对应要撤销的那笔报单的报单引用</p>
<p>FrontID: 对应要撤销的那笔报单的前置编号</p>
<p>SessionID: 对应要撤销的那笔报单的会话编号</p>
<p>ExchangeID: 对应要撤销的那笔报单的交易所ID</p>
<p>OrderSysID: 对应要撤销的那笔报单的报单编号</p>
<p>ActionFlag：只支持删除，不支持修改</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="e5cfe279-d814-41a6-bc35-5eae1c4b3463"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="725b0119-de09-454d-9909-67f4f184323c"></span>
## 4.调用示例
<p>//第一种方法，使用OrderSysID撤单（<strong><font style="color:red">推荐使用</font></strong>）</p>
<pre><code>CThostFtdcInputOrderActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.UserID, "1000001");
strcpy_s(a.OrderSysID, "         131");  //对应要撤报单的OrderSysID
strcpy_s(a.ExchangeID, "SHFE");
strcpy_s(a.InstrumentID, "rb1809");
ActionFlag = THOST_FTDC_AF_Delete;
m_pUserApi-&gt;ReqOrderAction(&amp;a, nRequestID++);
</code></pre>
<p>//第二种方法，使用FrontID+SessionID+OrderRef撤单</p>
<pre><code>CThostFtdcInputOrderActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.UserID, "1000001");
a.FrontID = 1;   //对应要撤报单的FrontID
a.SessionID = -788541;   //对应要撤报单的sessionid
strcpy_s(a.OrderRef, "        3");   //对应要撤报单的OrderRef
strcpy_s(a.ExchangeID, "SHFE");
strcpy_s(a.InstrumentID, "rb1809");
ActionFlag = THOST_FTDC_AF_Delete;
m_pUserApi-&gt;ReqOrderAction(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="e5672260-fb70-444f-8054-b44854acb684"></span>
## 5.FAQ
<p>无</p>
