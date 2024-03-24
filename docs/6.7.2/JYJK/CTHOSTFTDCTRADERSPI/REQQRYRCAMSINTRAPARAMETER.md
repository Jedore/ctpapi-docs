<p>请求RCAMS品种内风险对冲参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINTRAPARAMETER/">OnRspQryRCAMSIntraParameter</a></p>
<span class="anchor" id="923dcd22-a7a4-40b2-9395-2079d2debfbf"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSIntraParameter(CThostFtdcQryRCAMSIntraParameterField *pQryRCAMSIntraParameter, int nRequestID) = 0;</p>
<span class="anchor" id="92f9516a-2031-4dda-b60d-138330284e75"></span>
## 2.参数
<p>pQryRCAMSIntraParameter：RCAMS品种内风险对冲参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProductID</td>
<td style="TEXT-ALIGN: left;">产品组合代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="e003a9b7-eeb3-4277-af98-0f7e18e32580"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="343f4b67-d60f-4a76-9736-7a1de1396e64"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="f00c0338-1226-4289-9383-d8dbe78ea56e"></span>
## 5.FAQ
<p>无</p>
