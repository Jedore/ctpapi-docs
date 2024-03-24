<p>期权自对冲操作错误回报，当执行ReqOptionSelfCloseAction后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="e988fd53-4b16-4e5c-ade7-b106ff53e926"></span>
## 1.函数原型
<p>virtual void OnErrRtnOptionSelfCloseAction(CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="92a7dcf3-7b07-41e4-b44c-7aa83dd250a4"></span>
## 2.参数
<p>pOptionSelfCloseAction：期权自对冲操作</p>
<pre><code>struct CThostFtdcOptionSelfCloseActionField
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
    ///操作日期
    TThostFtdcDateType ActionDate;
    ///操作时间
    TThostFtdcTimeType ActionTime;
    ///交易所交易员代码
    TThostFtdcTraderIDType TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///本地期权自对冲编号
    TThostFtdcOrderLocalIDType OptionSelfCloseLocalID;
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
<p>ActionFlag：只有删除标志，修改标志位不支持</p>
<p>InstallID：CTP内部使用</p>
<p>StatusMsg：报错信息</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="542209cf-95d1-4ebd-9479-3dd14dca5832"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ae8f7fd1-8391-44a4-b250-1ad199be5190"></span>
## 4.FAQ
<p>无</p>
