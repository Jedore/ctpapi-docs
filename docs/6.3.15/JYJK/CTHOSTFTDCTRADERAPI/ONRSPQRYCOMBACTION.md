<p>请求查询申请组合响应，当执行ReqQryCombAction后，该方法被调用</p>
<span class="anchor" id="371c56e0-2047-4356-ac81-9791d8d786c4"></span>
## 1.函数原型
<p>virtual void OnRspQryCombAction(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="9fdd3f9f-1c72-47d0-b9c6-24ced3c547a9"></span>
## 2.参数
<p>pCombAction：申请组合</p>
<pre><code>struct CThostFtdcCombActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///组合引用
    TThostFtdcOrderRefType CombActionRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///数量
    TThostFtdcVolumeType Volume;
    ///组合指令方向
    TThostFtdcCombDirectionType CombDirection;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///本地申请组合编号
    TThostFtdcOrderLocalIDType ActionLocalID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType ClientID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///交易所交易员代码
    TThostFtdcTraderIDType TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///组合状态
    TThostFtdcOrderActionStatusType ActionStatus;
    ///报单提示序号
    TThostFtdcSequenceNoType NotifySequence;
    ///交易日
    TThostFtdcDateType TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType SettlementID;
    ///序号
    TThostFtdcSequenceNoType SequenceNo;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///用户端产品信息
    TThostFtdcProductInfoType UserProductInfo;
    ///状态信息
    TThostFtdcErrorMsgType StatusMsg;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
    ///组合编号
    TThostFtdcTradeIDType ComTradeID;
    ///营业部编号
    TThostFtdcBranchIDType BranchID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>CombDirection：确定是组合还是拆分命令</p>
<p>ActionStatus：组合单最后的报单结果</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="b8b7cd07-7ebc-46bc-931a-86e911815504"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f4f70307-61fb-429c-a8ec-a5251f12087f"></span>
## 4.FAQ
<p>无</p>
