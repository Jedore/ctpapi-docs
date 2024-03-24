<p>预埋撤单录入请求</p>
<p>响应: OnRspQryParkedOrderAction</p>
<span class="anchor" id="c3b58c54-98be-4457-addd-63644de77988"></span>
## 1.函数原型
<p>virtual int ReqParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="e14e0be6-81e4-44f1-a964-7cadc3cd8a99"></span>
## 2.参数
<p>pParkedOrderAction：输入预埋单操作</p>
<pre><code>struct CThostFtdcParkedOrderActionField
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
    ///预埋撤单单编号
    TThostFtdcParkedOrderActionIDType ParkedOrderActionID;
    ///用户类型
    TThostFtdcUserTypeType UserType;
    ///预埋撤单状态
    TThostFtdcParkedOrderStatusType Status;
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
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
<span class="anchor" id="e474a5b2-1a71-463c-9400-ab5e043acee2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="567e8278-c8b3-4b2e-ab01-7e7d08bcca65"></span>
## 4.调用示例
<pre><code>CThostFtdcParkedOrderActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.ExchangeID, "SHFE");
strcpy_s(a.OrderSysID, "    10061782"); 
strcpy_s(a.UserID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
ActionFlag = THOST_FTDC_AF_Delete;
m_pUserApi-&gt;ReqParkedOrderAction(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="e29352c6-fa6a-400c-bb6f-a9e8d7abc634"></span>
## 5.FAQ
<p>无</p>
