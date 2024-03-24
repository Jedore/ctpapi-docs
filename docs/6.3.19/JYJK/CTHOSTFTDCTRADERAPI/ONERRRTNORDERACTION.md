<p>报单操作错误回报，当执行ReqOrderAction后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="4356bb58-8980-49a5-8f21-0e381d15895c"></span>
## 1.函数原型
<p>virtual void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="e05c9cfe-039b-4224-9b36-7be2f009d7ae"></span>
## 2.参数
<p>pOrderAction：报单操作</p>
<pre><code>struct CThostFtdcOrderActionField
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
    ///操作日期
    TThostFtdcDateType ActionDate;
    ///操作时间
    TThostFtdcTimeType ActionTime;
    ///交易所交易员代码
    TThostFtdcTraderIDType TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///本地报单编号
    TThostFtdcOrderLocalIDType OrderLocalID;
    ///操作本地编号
    TThostFtdcOrderLocalIDType ActionLocalID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType ClientID;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///报单操作状态
    TThostFtdcOrderActionStatusType OrderActionStatus;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///状态信息
    TThostFtdcErrorMsgType StatusMsg;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///营业部编号
    TThostFtdcBranchIDType BranchID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>OrderSysID：交易所返回的报单编号</p>
<p>ActionFlag：撤单标志，现在只支持删除，不支持修改</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="63607e59-fe29-4f0e-a21f-84b08c26485d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="cf247fac-f62b-4c90-8d88-be4f73e1e2f9"></span>
## 4.FAQ
<p>无</p>
